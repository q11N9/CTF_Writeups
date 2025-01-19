We get a binary file with libc_32

![image](https://hackmd.io/_uploads/ByOoonIS1e.png)

Decompile to see what's inside the `main` function: 
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v4; // [esp-Ch] [ebp-44h]
  int v5; // [esp-Ch] [ebp-44h]
  int v6; // [esp-8h] [ebp-40h]
  int v7; // [esp-4h] [ebp-3Ch]
  char v8[32]; // [esp+Ch] [ebp-2Ch] BYREF
  unsigned int v9; // [esp+2Ch] [ebp-Ch]

  v9 = __readgsdword(0x14u);
  init();
  welcome();
  while ( 1 )
  {
    menu();
    __isoc99_scanf("%s", v8);
    switch ( atoi(v8) )
    {
      case 1:
        openfile();
        continue;
      case 2:
        readfile();
        continue;
      case 3:
        writefile();
        continue;
      case 4:
        closefile();
        continue;
      case 5:
        printf("Leave your name :");
        __isoc99_scanf("%s", name);
        printf("Thank you %s ,see you next time\n", name);
        if ( fp )
          fclose(fp);
        exit(0, v5, v6, v7);
        goto LABEL_10;
      default:
LABEL_10:
        puts("Invaild choice");
        exit(0, v4, v6, v7);
        break;
    }
  }
}
```

There is a overflow bug here, when it used `scanf` to take our input for `name`, but didn't limit the size of it. And you can see the space between `name` and `fp`

![image](https://hackmd.io/_uploads/SJTM328BJg.png)

Let's see other function. `openfile()`:  
```c
int openfile()
{
  int v1; // [esp-Ch] [ebp-14h]
  int v2; // [esp-8h] [ebp-10h]
  int v3; // [esp-4h] [ebp-Ch]

  if ( fp )
  {
    puts("You need to close the file first");
    return 0;
  }
  else
  {
    memset(&magicbuf, 0, 400);
    printf("What do you want to see :");
    __isoc99_scanf("%63s", &filename);
    if ( strstr(&filename, "flag") )
    {
      puts("Danger !");
      exit(0, v1, v2, v3);
    }
    fp = fopen(&filename, "r");
    if ( fp )
      return puts("Open Successful");
    else
      return puts("Open failed");
  }
}
```
Open file just open a file for us, if it does not contain `flag` in their name. 

`readfile()`: 
```c
int readfile()
{
  int result; // eax

  memset(&magicbuf, 0, 400);
  if ( !fp )
    return puts("You need to open a file first");
  result = fread(&magicbuf, 399, 1, fp);
  if ( result )
    return puts("Read Successful");
  return result;
}
```
It used `fread()` to read data from file. 

`closefile()`: 
```c
int closefile()
{
  int result; // eax

  if ( fp )
    result = fclose(fp);
  else
    result = puts("Nothing need to close");
  fp = 0;
  return result;
}
```
It set `fp` to 0 which closes file. 
Because we can overwrite `fp`, `fp` is `_IO_FILE_plus` struct, this can be seen in glibc 2.23 which is our libc version of this task: 

![image](https://hackmd.io/_uploads/BygzAuvSJx.png)

This is the struct of `_IO_FILE`: 

![image](https://hackmd.io/_uploads/HkMF0uDrJe.png)

`_IO_jump_t`: 

![image](https://hackmd.io/_uploads/Hkq-ZYPrJg.png)

It takes 2 parameters to jump to corresponding function. For example, if a function called `__IO_read_t`, it will called to `__read`
Now, if we can create a fake vtables and points `_IO_FILE_plus` to it, we can execute anything we want. 

Because after calling `fclose()`, it will exit immediately. We want to change the `fclose()` somehow to return to our main. 
When program calls to `fclose()`, a `_IO_new_close()` will be called instead:

![image](https://hackmd.io/_uploads/r1GsrQqr1x.png)

`_IO_new_close()`:
```c
_IO_new_fclose (_IO_FILE *fp)
{
  int status;

  CHECK_FILE(fp, EOF);

#if SHLIB_COMPAT (libc, GLIBC_2_0, GLIBC_2_1)
  /* We desperately try to help programs which are using streams in a
     strange way and mix old and new functions.  Detect old streams
     here.  */
  if (_IO_vtable_offset (fp) != 0)
    return _IO_old_fclose (fp);
#endif

  /* First unlink the stream.  */
  if (fp->_IO_file_flags & _IO_IS_FILEBUF)
    _IO_un_link ((struct _IO_FILE_plus *) fp);

  _IO_acquire_lock (fp);
  if (fp->_IO_file_flags & _IO_IS_FILEBUF)
    status = _IO_file_close_it (fp);
  else
    status = fp->_flags & _IO_ERR_SEEN ? -1 : 0;
  _IO_release_lock (fp);
  _IO_FINISH (fp);
  if (fp->_mode > 0)
    {
#if _LIBC
      /* This stream has a wide orientation.  This means we have to free
	 the conversion functions.  */
      struct _IO_codecvt *cc = fp->_codecvt;

      __libc_lock_lock (__gconv_lock);
      __gconv_release_step (cc->__cd_in.__cd.__steps);
      __gconv_release_step (cc->__cd_out.__cd.__steps);
      __libc_lock_unlock (__gconv_lock);
#endif
    }
  else
    {
      if (_IO_have_backup (fp))
	_IO_free_backup_area (fp);
    }
  if (fp != _IO_stdin && fp != _IO_stdout && fp != _IO_stderr)
    {
      fp->_IO_file_flags = 0;
      free(fp);
    }

  return status;
}
```
it returns `status`, which is set by `_IO_file_close_it`, or `_IO_new_file_close_it`:

![image](https://hackmd.io/_uploads/r1eN87qBke.png)

```c
_IO_new_file_close_it (_IO_FILE *fp)
{
  int write_status;
  if (!_IO_file_is_open (fp))
    return EOF;

  if ((fp->_flags & _IO_NO_WRITES) == 0
      && (fp->_flags & _IO_CURRENTLY_PUTTING) != 0)
    write_status = _IO_do_flush (fp);
  else
    write_status = 0;

  _IO_unsave_markers (fp);

  int close_status = ((fp->_flags2 & _IO_FLAGS2_NOCLOSE) == 0
		      ? _IO_SYSCLOSE (fp) : 0);

  /* Free buffer. */
#if defined _LIBC || defined _GLIBCPP_USE_WCHAR_T
  if (fp->_mode > 0)
    {
      if (_IO_have_wbackup (fp))
	_IO_free_wbackup_area (fp);
      _IO_wsetb (fp, NULL, NULL, 0);
      _IO_wsetg (fp, NULL, NULL, NULL);
      _IO_wsetp (fp, NULL, NULL);
    }
#endif
  _IO_setb (fp, NULL, NULL, 0);
  _IO_setg (fp, NULL, NULL, NULL);
  _IO_setp (fp, NULL, NULL);

  _IO_un_link ((struct _IO_FILE_plus *) fp);
  fp->_flags = _IO_MAGIC|CLOSED_FILEBUF_FLAGS;
  fp->_fileno = -1;
  fp->_offset = _IO_pos_BAD;

  return close_status ? close_status : write_status;
}
```
`close_status` depends on `_IO_SYSCLOSE()`: 

![image](https://hackmd.io/_uploads/S1DK9m5r1g.png)

Instead of execute `__close`, we can change our fake vtables to `main` so it will return to our main function instead of go to that `__close`. 

there is a `fread()` in our program: 

![image](https://hackmd.io/_uploads/Hk2gFQqrke.png)

Let's analyze `fread()`: 

![image](https://hackmd.io/_uploads/r1ObqQcr1x.png)

![image](https://hackmd.io/_uploads/rJz3qmcH1l.png)

`_IO_sgetn` seems like we can overwrite: 

![image](https://hackmd.io/_uploads/SkYMsmqrke.png)

It is corresponding to `_IO_XSGETN`, which is: 

![image](https://hackmd.io/_uploads/rJVvs79B1e.png)

`__xsgetn` in vtables. 
We can overwrite it to `printf.plt`, by using format string, it will give us a libc address. 
For summary: 
- Create a fake `IO_FILE_plus` then points `fp` to it
- Overwrite first 4 bytes of `fp` to format string to leak libc
- Overwrite fake vtable with `__close` -> `main`, `__xsgetn` -> `printf.plt`
- Except 

| Address   | Old data | New data |
| -------- | -------- | -------- |
| 0x804b260| name     |`A`\*0x20 |
| ...      |          |  |
| 0x804b280| fp     | 0x804b290     |
|...
|0x804b290 |\_flags | format string
|0x804b294|\_IO_read_ptr| fclose's address
|0x804b298|\_IO_read_end|fclose's address + 400
|0x804b29c|\_IO_read_base| fclose's address
|...| ...| padding|
|0x804b2d8| \_lock| magicbuf's address
|...|...|padding
|0x804b324| \*vtables|fp's address + 168|
|...|\_\_dummy1 and \_\_dummy2 |padding
|...|...|some r-x address
|0x804b348|\_\_xsgetn|printf.plt
|...|...|some r-x address 
|0x804b36c|\_\_close|main's address
|...|...|some r-x address

Set breakpoint in `fread()` to calculate the offset format string to leak libc: 

Our payload will be like this 

![image](https://hackmd.io/_uploads/r1xIALKBkl.png)

Because `_xsgetn` has been changed to `printf_plt`, we can now get the libc leak: 

![image](https://hackmd.io/_uploads/Sy2FRUFBkl.png)

To get shell, we just need to change our format string to parameter of `system()`, which is `sh\0\0` (need 4 bytes because this is x86 system). And change the `_close` to `system()`

![image](https://hackmd.io/_uploads/rk0ACIYBJe.png)

After getting the shell, we must pass another check in `get_flag`, but they give us the source: 
```c
#include <unistd.h>
#include <stdio.h>

int read_input(char *buf,unsigned int size){
    int ret ;
    ret = read(0,buf,size);
    if(ret <= 0){
        puts("read error");
        exit(1);
    }
    if(buf[ret-1] == '\n')
        buf[ret-1] = '\x00';
    return ret ;
}

int main(){
	char buf[100];
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	printf("Your magic :");
	read_input(buf,40);
	if(strcmp(buf,"Give me the flag")){
		puts("GG !");
		return 1;
	}
	FILE *fp = fopen("/home/seethefile/flag","r");
	if(!fp){
		puts("Open failed !");
	}
	fread(buf,1,40,fp);
	printf("Here is your flag: %s \n",buf);
	fclose(fp);
}

```

Full script: [solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/pwnable.tw/seethefile/solve.py))
