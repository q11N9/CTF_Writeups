We have a binary file 64 bit and libc version 2.29. We decompile it: 

![image](https://hackmd.io/_uploads/HkwRVSWr1l.png)

`main()` function: 
```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  int choice; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v4; // [rsp+8h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  choice = 0;
  init_proc(argc, argv, envp);
  while ( 1 )
  {
    while ( 1 )
    {
      menu();
      __isoc99_scanf("%d", &choice);
      if ( choice != 2 )
        break;
      reallocate();
    }
    if ( choice > 2 )
    {
      if ( choice == 3 )
      {
        rfree();
      }
      else
      {
        if ( choice == 4 )
          _exit(0);
LABEL_13:
        puts("Invalid Choice");
      }
    }
    else
    {
      if ( choice != 1 )
        goto LABEL_13;
      allocate();
    }
  }
}
```
go into `allocate()`: 
```c
int allocate()
{
  _BYTE *v0; // rax
  unsigned __int64 v2; // [rsp+0h] [rbp-20h]
  unsigned __int64 size; // [rsp+8h] [rbp-18h]
  void *v4; // [rsp+18h] [rbp-8h]

  printf("Index:");
  v2 = read_long();
  if ( v2 > 1 || heap[v2] )
  {
    LODWORD(v0) = puts("Invalid !");
  }
  else
  {
    printf("Size:");
    size = read_long();
    if ( size <= 0x78 )
    {
      v4 = realloc(0LL, size);
      if ( v4 )
      {
        heap[v2] = v4;
        printf("Data:");
        v0 = (_BYTE *)(heap[v2] + read_input(heap[v2], size));
        *v0 = 0;
      }
      else
      {
        LODWORD(v0) = puts("alloc error");
      }
    }
    else
    {
      LODWORD(v0) = puts("Too large!");
    }
  }
  return (int)v0;
}
```
They use realloc to allocate a chunk, limited with only 2 chunk and with the size not greater than `0x78`. And then `v0` is used to null terminator our input. 
`reallocate()` function: 
```c
int reallocate()
{
  unsigned __int64 v1; // [rsp+8h] [rbp-18h]
  unsigned __int64 size; // [rsp+10h] [rbp-10h]
  void *v3; // [rsp+18h] [rbp-8h]

  printf("Index:");
  v1 = read_long();
  if ( v1 > 1 || !heap[v1] )
    return puts("Invalid !");
  printf("Size:");
  size = read_long();
  if ( size > 0x78 )
    return puts("Too large!");
  v3 = realloc((void *)heap[v1], size);
  if ( !v3 )
    return puts("alloc error");
  heap[v1] = v3;
  printf("Data:");
  return read_input(heap[v1], size);
}
```
It will realloc our input heap index. But it doesn't check the case index 0 overlap the data of index 1. 
`rfree()`: 
```c
int rfree()
{
  _QWORD *v0; // rax
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  printf("Index:");
  v2 = read_long();
  if ( v2 > 1 )
  {
    LODWORD(v0) = puts("Invalid !");
  }
  else
  {
    realloc((void *)heap[v2], 0LL);
    v0 = heap;
    heap[v2] = 0LL;
  }
  return (int)v0;
}
```
it uses `realloc()` with 0 as size to free a chunk, and nulldify the chunk. 
Let's see the structure of a chunk when we alloc and rfree: 
First, i malloc a chunk with size 32: 

![image](https://hackmd.io/_uploads/S1m_uB-BJg.png)

![image](https://hackmd.io/_uploads/Sy5__SWr1l.png)

So the size of our chunk is `0x20 + 0x10 of metadata = 0x30`. 
I allocate one more and free the first one:

 ![image](https://hackmd.io/_uploads/SkvT_rWrkx.png)
 
So now, the index 0 is freed. Note that there is no UAF here because the pointer to index 0 is removed: 

![image](https://hackmd.io/_uploads/HJiSFBbrkx.png)

My idea is to modify the metadata of index 1, make it size to `0x420` to bypass tcache bin. To do that, let's malloc a chunk with size `0x30`: 

![image](https://hackmd.io/_uploads/rys1qBZr1x.png)

But i was wrong, i forgot it doesn't take the index 0's chunk. But...this give me an idea. I can free then malloc again, free then malloc again to create a fake chunk for unsorted bin. To do that, first, let's retry to modify the metadata of index 1. 

![image](https://hackmd.io/_uploads/rylT5HZHJg.png)

Check in heap: 

![image](https://hackmd.io/_uploads/HkGXorZryx.png)

Hmmm, I don't know it will free the previous one and malloc one more. 

After struggling, i know that if i realloc a chunk with size 0, it does not affect the pointer in `heap`. 

![image](https://hackmd.io/_uploads/r1Z3ISMSye.png)

![image](https://hackmd.io/_uploads/H17sUSfSke.png)

You can see the different between this time and `rfree()`, there is still pointer in `heap`. So now if i realloc as the same size before(48),because it only check if exists `heap[v1]` or not, i can modify a freed chunk. We have UAF here!

![image](https://hackmd.io/_uploads/SypyOBGS1x.png)

![image](https://hackmd.io/_uploads/BJdxOBzSkg.png)

Now i use a technique called [tcache poisoning](https://github.com/shellphish/how2heap/blob/master/glibc_2.27/tcache_poisoning.c). Because we can modify freed chunk, so we can modify it into an address that we want to control.
So I will overwrite the atoll.got to printf.plt. First, we put `atoll.got` into tcache: 

![image](https://hackmd.io/_uploads/SyhyBV4Hye.png)

![image](https://hackmd.io/_uploads/S1xGBEEHJe.png)

![image](https://hackmd.io/_uploads/ryBmrENrJe.png)

I will explain why the size is 0x20 later. Note that in mind. 
After this step, in tcache is still have a valid chunk. We want to put it out, so we can alloc chunk index 1

![image](https://hackmd.io/_uploads/By_cSEEH1x.png)

So now, all 2 indexes is filled. We must reset them to reuse later.

![image](https://hackmd.io/_uploads/BJ7AHEVrke.png)

The process i just used is poisoning `0x20` tcache. 

![image](https://hackmd.io/_uploads/r1DDLVVHJg.png)

Now we just need to put out that chunk in tcache `0x20`, overwrite its data with `printf.plt`, we now change `atoll` to `printf`:

![image](https://hackmd.io/_uploads/SJT4PNVrJx.png)

If you wonder why it's 0x40, i will explain it later too, with 0x10 on there. :accept:
Now, we can check in gdb: 

![image](https://hackmd.io/_uploads/S1r1u44BJx.png)

You can see now the chunk `0x404048` is taken out from tcache, and index 0 points to:

![image](https://hackmd.io/_uploads/S1dXOVEryl.png)

And we succesfully change atoi.got to printf.plt

![image](https://hackmd.io/_uploads/rJFHu4VSJl.png)

In this step, you can use format string bug to leak out the libc address: 

![image](https://hackmd.io/_uploads/SJX0uEVB1e.png)

In my program, i use a libc address. But you can use `%..$p` 

![image](https://hackmd.io/_uploads/Hyv0AdESyx.png)

We have system address~ Now let's execute `system('/bin/sh')`. Because `atoll` is modified, so we cannot send index to the input. But `alloc()` function only checks if `heap[index]` exists or not. So we just need to alloc one more without index. But, how about the size? I was struggling in there because my program seg fault all times. I knew `atoll` is overwritten by `printf`, but i don't know why when i malloc one more, it doesn't seems like give us a shell because there are some reasons: 
First, printf will return how many characters in your strings inputted in. BUT, when you alloc to overwrite `atoll` again, it can just malloc for you a `0x20` chunk (counted metadata). 

![image](https://hackmd.io/_uploads/rJq3bt4Hkl.png)

![image](https://hackmd.io/_uploads/HJe6bYVrJg.png)

You can see that it will malloc a new chunk on heap, not take out the chunk in tcache. So that's why i need to poison `0x20` tcache bin on there. It's leading to why i must taken out the `atoll.got` in `0x40` because i must use `0x20` later. 

![image](https://hackmd.io/_uploads/HykvzKErye.png)

The tcache you poisoned should be like this. Except the first one, other can be different. 
Like i talked before, `printf` will return the number of characters you input in, so i just only overwrite 8 bytes of `atoll.got` to `system`. This took me a lot of time to realize. 

![image](https://hackmd.io/_uploads/rJbVXK4HJl.png)

![image](https://hackmd.io/_uploads/Bys0mYVSyl.png)

Script: [solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/pwnable.tw/Re-alloc/solve.py)
