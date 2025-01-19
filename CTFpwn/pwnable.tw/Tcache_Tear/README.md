We have given libc(2.27) and binary file. Decompile:  

![image](https://hackmd.io/_uploads/H1kNhF4Hkg.png)

```c
void __fastcall __noreturn main(__int64 a1, char **a2, char **a3)
{
  __int64 v3; // rax
  unsigned int v4; // [rsp+Ch] [rbp-4h]

  set_buf(a1, a2, a3);
  printf("Name:");
  readinp(&name, 32LL);
  v4 = 0;
  while ( 1 )
  {
    while ( 1 )
    {
      menu();
      v3 = convert_long();
      if ( v3 != 2 )
        break;
      if ( v4 <= 7 )
      {
        free(ptr);                              
        ++v4;
      }
    }
    if ( v3 > 2 )
    {
      if ( v3 == 3 )
      {
        view();
      }
      else
      {
        if ( v3 == 4 )
          exit(0);
LABEL_14:
        puts("Invalid choice");
      }
    }
    else
    {
      if ( v3 != 1 )
        goto LABEL_14;
      create();
    }
  }
}
```

Easy to know that, there is a UAF bug here. And it only let us free 8 chunks in total. It only frees the last chunk created so we cannot choose which one to free.
Let's check another function. 
`create()`: 

```c
int sub_400B14()
{
  size_t v0; // rax
  int size; // [rsp+8h] [rbp-8h]

  printf("Size:");
  v0 = convert_long();
  size = v0;
  if ( v0 <= 0xFF )
  {
    ptr = malloc(v0);
    printf("Data:");
    readinp(ptr, (unsigned int)(size - 16));
    LODWORD(v0) = puts("Done !");
  }
  return v0;
}
```
We can only malloc a smaller `0xff` chunk. 
`view()`: 
```c!
ssize_t view()
{
  printf("Name :");
  return write(1, &name, 0x20uLL);
}
```

It just prints out our name. 

This is libc 2.27, so we can use double-free vulnerability. Because it doesn't delete ptr to freed chunk, we can free a chunk twice. About double-free you can read more in [here](https://guyinatuxedo.github.io/27-edit_free_chunk/double_free_explanation/index.html). Of course, this is for higher libc version. From 2.29, there is mechanism that checks bins to prevent double free

![image](https://hackmd.io/_uploads/r159siHHkg.png)

To demonstrate, if you create a chunk and free them 2 times, you can see it points to itself.

![image](https://hackmd.io/_uploads/BJh-njrSJx.png)

So if we can change that value in `0x603260`, make it points to a fake chunk so then when we take it out, free it, it will go into unsorted bin. 
To do that, first, we must create a fake chunk. Because we can only `view()` for `name`, this will be our perfect target. 
To make a fake chunk, we need a start and end unsorted bin:
- `name` will keep the metadata of the fake chunk

 ![image](https://hackmd.io/_uploads/r1rqWnrBye.png)

- Our fake chunk will be like this
```

name address: |metadata    |
name + 0x10 : |     0      |    <- actual pointer in tcache
...
name + 0x500: |metadata of small chunk 1|
name + 0x510: |data of small chunk 1    |
name + 0x520: |metadata of small chunk 2|
```
Why we need 2 small chunks? Why don't use 1 chunk just to limit? I tried and always get double free or corruption. My explaination is, when a chunk is freed, the chunk after it will have the metadata like this 

![image](https://hackmd.io/_uploads/SJslEnSHJx.png)

So, if we don't make a small chunk 2, and make small chunk 1 is overlapped by our fake chunk, when we free it, we will get error because it will try to consolidate it with top chunk (because there is no chunk after it). And the small chunk 2, its role is limitting our fake chunk in 0x500. 
This is how to make a fake chunk. 

![image](https://hackmd.io/_uploads/rkWqN2HrJx.png)

We use double free to write data in `name_addr+0x500` with small chunk 1 and chunk 2. 

![image](https://hackmd.io/_uploads/HkvA43HSkl.png)

Next time, we must use another index of tcache because this `0x50` tcache is corrupted and cannot be used anymore. 

![image](https://hackmd.io/_uploads/ByvuShrSJl.png)

![image](https://hackmd.io/_uploads/HkuLHhBHkx.png)

You can check my explaination: 

![image](https://hackmd.io/_uploads/H11cShHSyl.png)

That `500` is the previous size, and `0x20` is the size of small chunk 1 and from `0x21` to `0x20` because previous chunk is not in used. 
Now we just need to show info and get libc leak. 

![image](https://hackmd.io/_uploads/SkbgP3BrJe.png)

Because FullRelRO is enabled, we cannot overwrite GOT. So we must overwrite `free_hook` to one gadget to get shell. 
![image](https://hackmd.io/_uploads/r1TUh3HSJl.png)

![image](https://hackmd.io/_uploads/HkvD32HBJg.png)

Script: [solve.py](https://github.com/q11N9/CTF_Writeups/new/main/CTFpwn/pwnable.tw/Tcache_Tear/solve.py)

I searched and read some writeups and know that there is another way to solve this challenge without overwritting `name` variable. The idea is using FILE struct attack. For more information, you can read it in [here](https://hackmd.io/@y198/HkR3Bz1-s)(in Vietnamese)
In conclusion, we must bypass this 

![image](https://hackmd.io/_uploads/r1OGApSHkl.png)

So we must set `fp->flags` to `0xfbad1800`, which is the value of `IO_IS_APPENDING`, and overwrite the last byte of `_IO_write_base` to `\x00` so we can leak out `_IO_stdfile_2_lock`. After modify it, the `__IO_2_1_stdout_` will be like this 
```bash
p _IO_2_1_stdout_ 
$1 = {
  file = {
    _flags = 0xfbad1800,
    _IO_read_ptr = 0x7c21d2bec7e3 <_IO_2_1_stdout_+131> "\n",
    _IO_read_end = 0x7c21d2bec7e3 <_IO_2_1_stdout_+131> "\n",
    _IO_read_base = 0x7c21d2bec7e3 <_IO_2_1_stdout_+131> "\n",
    _IO_write_base = 0x7c21d2bec7e3 <_IO_2_1_stdout_+131> "\n",
    _IO_write_ptr = 0x7c21d2bec7e3 <_IO_2_1_stdout_+131> "\n",
    _IO_write_end = 0x7c21d2bec7e4 <_IO_2_1_stdout_+132> "",
    _IO_buf_base = 0x7c21d2bec7e3 <_IO_2_1_stdout_+131> "\n",
    _IO_buf_end = 0x7c21d2bec7e4 <_IO_2_1_stdout_+132> "",
    _IO_save_base = 0x0,
    _IO_backup_base = 0x0,
    _IO_save_end = 0x0,
    _markers = 0x0,
    _chain = 0x7c21d2beba00 <_IO_2_1_stdin_>,
    _fileno = 0x1,
    _flags2 = 0x0,
    _old_offset = 0xffffffffffffffff,
    _cur_column = 0x0,
    _vtable_offset = 0x0,
    _shortbuf = "\n",
    _lock = 0x7c21d2bed8c0 <_IO_stdfile_1_lock>,
    _offset = 0xffffffffffffffff,
    _codecvt = 0x0,
    _wide_data = 0x7c21d2beb8c0 <_IO_wide_data_1>,
    _freeres_list = 0x0,
    _freeres_buf = 0x0,
    __pad5 = 0x0,
    _mode = 0xffffffff,
    _unused2 = '\000' <repeats 19 times>
  },
  vtable = 0x7c21d2be82a0 <__GI__IO_file_jumps>
}

```

![image](https://hackmd.io/_uploads/BydC7ABr1g.png)

![image](https://hackmd.io/_uploads/B10070rSke.png)

Other step is the same. 
Script 2: [solve2.py](https://github.com/q11N9/CTF_Writeups/edit/main/CTFpwn/pwnable.tw/Tcache_Tear/solve2.py)
