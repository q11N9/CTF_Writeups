We have a binary file and glibc. Decompile it: 

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  int v3; // eax

  setup(argc, argv, envp);
  banner();
  while ( 1 )
  {
    while ( 1 )
    {
      v3 = menu();
      if ( v3 != 4 )
        break;
      copy_paste();
    }
    if ( v3 > 4 )
    {
LABEL_12:
      error("Invalid option");
    }
    else
    {
      switch ( v3 )
      {
        case 3:
          view();
          break;
        case 1:
          create();
          break;
        case 2:
          delete();
          break;
        default:
          goto LABEL_12;
      }
    }
  }
}
```
This is a heap challenge, which let us create, delete, view and copy-paste heap chunks.

![image](https://hackmd.io/_uploads/BkzV5H24ke.png)

Check in `create()`: 
```c
unsigned __int64 create()
{
  int journal_day; // eax
  void *v1; // rax
  unsigned int index; // [rsp+Ch] [rbp-14h] BYREF
  Journal *journal; // [rsp+10h] [rbp-10h]
  unsigned __int64 v5; // [rsp+18h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  puts("Journal index:");
  index = 0;
  __isoc99_scanf("%d", &index);
  if ( index < 10 )
  {
    if ( Chunks[index] && Chunks[index]->flag )
    {
      error("Journal index occupied");
    }
    else
    {
      journal = (Journal *)malloc(0x18uLL);
      journal_day = day++;
      journal->status = journal_day;
      puts("Journal size:");
      __isoc99_scanf("%lu", &journal->size);
      v1 = malloc(journal->size);
      journal->data = v1;
      journal->flag = 1;
      if ( !journal->data )
      {
        error("Could not allocate space for journal");
        exit(-1);
      }
      puts("Enter your data:");
      read(0, journal->data, journal->size);
      Chunks[index] = journal;
      putchar(10);
    }
  }
  else
  {
    error("Journal index out of range");
  }
  return __readfsqword(0x28u) ^ v5;
}
```
The struct of a `journal`:

![image](https://hackmd.io/_uploads/rkEFqB34Je.png)

In `delete()`:
```c
unsigned __int64 delete()
{
  unsigned int v1; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Journal index:");
  v1 = 0;
  __isoc99_scanf("%d", &v1);
  if ( v1 < 0xA )
  {
    if ( Chunks[v1] && Chunks[v1]->flag )
    {
      Chunks[v1]->flag = 0;
      free(Chunks[v1]->data);
    }
    else
    {
      error("Journal is not inuse");
    }
  }
  else
  {
    error("Journal index out of range");
  }
  return __readfsqword(0x28u) ^ v2;
}
```
We have a UAF bug here
In `view()`, nothing's special
In `copy_paste()`:
```c
unsigned __int64 copy_paste()
{
  unsigned int copy_idx; // [rsp+0h] [rbp-10h] BYREF
  unsigned int paste_idx; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v3; // [rsp+8h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  copy_idx = 0;
  paste_idx = 0;
  puts("Copy index:");
  __isoc99_scanf("%d", &copy_idx);
  if ( copy_idx >= 0xA || (puts("Paste index:"), __isoc99_scanf("%d", &paste_idx), paste_idx >= 0xA) )
  {
    error("Index out of range");
  }
  else if ( Chunks[copy_idx] && Chunks[paste_idx] )
  {
    if ( Chunks[copy_idx]->flag || Chunks[paste_idx]->flag )
    {
      if ( Chunks[copy_idx]->size <= Chunks[paste_idx]->size )
      {
        Chunks[paste_idx]->status = day;
        memcpy(Chunks[paste_idx]->data, Chunks[copy_idx]->data, Chunks[copy_idx]->size);
        puts("Copy successfull!\n");
      }
      else
      {
        error("Copy index size cannot be larger than the paste index size");
      }
    }
    else
    {
      error("Journal index not in use");
    }
  }
  else
  {
    error("Invalid copy/paste index");
  }
  return __readfsqword(0x28u) ^ v3;
}
```

So it will check if any of element is occupied, it will copy from one to another. So we can free a chunk into unsorted bin then copy it into a journal that being used. So we can leak the libc. 
But i was struggling when trying to put data out from unsorted bin

![image](https://hackmd.io/_uploads/Byxcir2EJe.png)

So i read Quang's writeup to see how he leaked libc address. So basically, we just need to create a very big chunk, which is out of range of fastbin so we can put it in the unsorted bin.

![image](https://hackmd.io/_uploads/ByiW2BnNJe.png)

Now, because it's libc 2.27, so we can overwrite `__malloc_hook` and `__free_hook`. I was tried overwritting all one_gadget to `--level 1` to `__malloc_hook` but it didn't work btw. So i overwrite `__free_hook` with `system()` to get shell. 

![image](https://hackmd.io/_uploads/HJpvZU3VJl.png)

![image](https://hackmd.io/_uploads/ryE8ZLn4Jl.png)

Script: [solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/HTB_University_CTF_2024/PrisonBreak/solve.py)
