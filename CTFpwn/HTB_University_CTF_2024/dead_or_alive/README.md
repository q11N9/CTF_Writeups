We decompile the binary file: 

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  int choice; // eax

  setup(argc, argv, envp);
  banner();
  while ( 1 )
  {
    while ( 1 )
    {
      choice = menu();
      if ( choice != 3 )
        break;
      view();
    }
    if ( choice > 3 )
    {
LABEL_10:
      error("Invalid option");
    }
    else if ( choice == 1 )
    {
      create();
    }
    else
    {
      if ( choice != 2 )
        goto LABEL_10;
      delete();
    }
  }
}
```

We can create, delete, view a Bounty.

![image](https://hackmd.io/_uploads/r1gKyiYTNye.png)

Function `create()`: 
```c
unsigned __int64 create()
{
  char *descriptionChunk; // rax
  bool status; // [rsp+7h] [rbp-29h]
  __int64 amount; // [rsp+8h] [rbp-28h] BYREF
  unsigned __int64 size; // [rsp+10h] [rbp-20h] BYREF
  Bounty *Bounty; // [rsp+18h] [rbp-18h]
  __int16 buf; // [rsp+26h] [rbp-Ah] BYREF
  unsigned __int64 v7; // [rsp+28h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  if ( (unsigned int)bounty_idx > 49 )
  {
    error("Maximum number of bounty registrations reached. Shutting down...");
    exit(-1);
  }
  printf("Bounty amount (Zell Bars): ");
  amount = 0LL;
  __isoc99_scanf("%lu", &amount);
  printf("Wanted alive (y/n): ");
  buf = 0;
  read(0, &buf, 2uLL);
  HIBYTE(buf) = 0;
  status = strcmp((const char *)&buf, "y") == 0;
  printf("Description size: ");
  size = 0LL;
  __isoc99_scanf("%lu", &size);
  if ( size <= 0x64 )
  {
    Bounty = (Bounty *)malloc(0x20uLL);
    if ( !Bounty )
    {
      error("Failed to allocate space for bounty");
      exit(-1);
    }
    Bounty->amount = amount;
    Bounty->status = status;
    Bounty->size = size;
    descriptionChunk = (char *)malloc(Bounty->size);
    Bounty->descriptionPtr = descriptionChunk;
    Bounty->active = 1;
    if ( !Bounty->descriptionPtr )
    {
      error("Failed to allocate space for bounty description");
      exit(-1);
    }
    puts("Bounty description:");
    read(0, Bounty->descriptionPtr, Bounty->size);
    Bounties[bounty_idx] = Bounty;
    printf("Bounty ID: %d\n\n", (unsigned int)bounty_idx);
    ++bounty_idx;
  }
  else
  {
    error("Description size exceeds size limit");
  }
  return __readfsqword(0x28u) ^ v7;
}
```
Struct of a Bounty: 

![image](https://hackmd.io/_uploads/SkonitpVkx.png)

This function allows us to create a Bounty, then add the recently created one into Bounties index, with maximum size is 50 elements. 
- Each element is `0x20` big. This is the metadata of Bounty
- The `descriptionPtr` points to the chunk that contains data of Bounty. 
- After creating, it will add it into Bounties array. 
The chunk of a Bounty will be look like this:

![image](https://hackmd.io/_uploads/SkkfTtaNye.png)

![image](https://hackmd.io/_uploads/SksVpt64kg.png)

in `0x55555555a298` is contains the size of metadata of Bounty, which is `0x20 + 0x10 of metadata of heap chunk`. Next, the `0x000055555555a2d0` will point to the data of Bounty. Then `Bounty->amount`, `Bounty->size` which is `0x32 = 50`. The next is contains `active` and `status`, which is `0x01` and `0x01`.

Let's analyze the `delete()` function:  
```c
unsigned __int64 delete()
{
  unsigned int v1; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  printf("Bounty ID: ");
  v1 = 0;
  __isoc99_scanf("%d", &v1);
  if ( (v1 & 0x80000000) == 0 && v1 < bounty_idx )
  {
    if ( Bounties[v1]->active == 1 && Bounties[v1]->descriptionPtr )
    {
      free(Bounties[v1]->descriptionPtr);
      Bounties[v1]->descriptionPtr = 0LL;
      Bounties[v1]->active = 0;
      free(Bounties[v1]);
      putchar(10);
    }
    else
    {
      error("Invalid ID");
    }
  }
  else
  {
    error("Bounty ID out of range");
  }
  return __readfsqword(0x28u) ^ v2;
}
```
So first it checks the index, with condition 
`v1 < min(bounty_idx, 2^31)`
then checking if the `Bounty->active` is equals to 1 or not, and if there is existing pointer to data chunk, it first free the chunk data, nulldify the pointer to that chunk (not in array `Bounties`) and change the status to 0. Then it will free the metadata chunk (the chunk `0x20` talked before). 

Finally, the `view()` function: 
```c
unsigned __int64 view()
{
  const char *v0; // rax
  unsigned int v2; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v3; // [rsp+8h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  printf("Bounty ID: ");
  v2 = 0;
  __isoc99_scanf("%d", &v2);
  if ( v2 < 0x32 )
  {
    if ( Bounties[v2] )
    {
      if ( Bounties[v2]->active != 1 )
      {
        error("Bounty has been removed");
      }
      else
      {
        if ( Bounties[v2]->status )
          v0 = "Yes";
        else
          v0 = "No";
        printf(
          "\nBounty: %lu Zell Bars\nWanted alive: %s\nDescription: %s\n",
          Bounties[v2]->amount,
          v0,
          Bounties[v2]->descriptionPtr);
      }
    }
    else
    {
      error("Bounty ID does not exist");
    }
  }
  else
  {
    error("ID out of range");
  }
  return __readfsqword(0x28u) ^ v3;
}
```
it will view only the `Bounty` with index smaller than 0x32, then it will check if exists that pointer in `Bounties` array. If it exists, it checks `Bounty->active`, if equals to 1m it next check the `status` to print out later, not affect our condition. Then it will print out the `Bounty->amount` then `Bounty->description`

So there is no UAF or OOB,... for us to exploit. Our idea is first leaking the libc address. This is libc version 2.35

![image](https://hackmd.io/_uploads/HJCtGspV1x.png)

so we must pass the tcache mechanism. We must somehow put a chunk in unsorted bin, then we can leak the libc. But program limits our `description` size: 

![image](https://hackmd.io/_uploads/BywsM564Je.png)

Maybe there is a bug that let us modify a chunk then we can make a very big chunk to free, it will put it in unsorted bin. 
Look more closely in the `create()` and `delete()`, when first it will malloc the metadata chunk (size `0x20`), then free it.

![image](https://hackmd.io/_uploads/ry4ZzcTNyg.png)

![image](https://hackmd.io/_uploads/SklzfcpVJe.png)

So if we malloc 2 chunks, then free the first one, it will take out the chunk metadata of the first one. We can leak out some data: 

![image](https://hackmd.io/_uploads/rJt3XcTVkx.png)

![image](https://hackmd.io/_uploads/rJR1ucp4kl.png)

Check in gdb, it is some heap address: 

![image](https://hackmd.io/_uploads/HyLGdc641l.png)

In the address `0x55555555a2a0`, it is our leaking data. If we check in `Bounties` array: 

![image](https://hackmd.io/_uploads/HJfLO5641l.png)

The data pointer of index 1 and index 2 points to the same address
The process will be: 
- After free, the tcache will hold 4 freed chunks, each 2 of them are the same size. After we malloc a chunk `0x20` for index 2, it first need a chunk `0x20 + 0x10` to contains metadata, then malloc a chunk size `0x20(our input) + 0x10` to make a chunk for data of index 2. Luckily, in tcache, there are 2 chunks (metadata of index 0 and 1) which is satisfied our demand 

![image](https://hackmd.io/_uploads/rJSCPqaVyl.png)

Because we first freed index 0, then index 1. So when we create index 2, it first takes out the metadata of index 1 to create its metadata, then because of the `Bounties[2]->size` equals to the same as metadata of `index 0`, it will take out from tcache so the data leaked out is the metadata of index 0 after free. We can look at the tcache after create index 2: 

![image](https://hackmd.io/_uploads/rkjWtqTEJx.png)

That 2 `0x30` size chunks have been taken out 
The leaked data is some heap address. Because this is 2.35 libc, there is a mechanism to avoid UAF bug, it called [safe linking](https://elixir.bootlin.com/glibc/glibc-2.35/source/malloc/malloc.c#L349)

So to decrypt it, we use exploiting script from [how2heap](https://github.com/shellphish/how2heap/blob/master/glibc_2.35/decrypt_safe_linking.c)

![image](https://hackmd.io/_uploads/H1Vtc9aVyx.png)

So now we can leak out the heap address: 

![image](https://hackmd.io/_uploads/SJAFj5aEyx.png)

![image](https://hackmd.io/_uploads/BklFoqpEJe.png)

Check in gdb: 

![image](https://hackmd.io/_uploads/HJZXhqaNyx.png)

Something's wrong here =w=', i don't know why. Maybe my leaking address is wrong. Maybe because of heap consolidation... 
So i malloc one more in the first, then doing the same process. 
Now the data leaked is the metadata in index1, the metadata of index 2 will hold the metadata of index 3. This graph will simplify the heap after free 3 chunks first: 
```c
| Freed metadata of Bounties[0]  |
| Freed Bounties[0]->description |
| Freed metadata of Bounties[1]  |
| Freed Bounties[1]->description |
| Freed metadata of Bounties[2]  |
| Freed Bounties[2]->description |
```
After we malloc `Bounties[3]`, the heap will be look like this 
```c!
|Freed metadata of Bounties[0] |
|Freed Bounties[0]->description|
|    Data of Bounties[3]       |
|Freed Bounties[1]->description|
|     Metadata of Bounties[3]  |
|Freed Bounties[2]->description|
```
Checking in gdb: The heap after remove 3 first chunk: 

![image](https://hackmd.io/_uploads/BJgPOCp41e.png)

After create `Bounties[3]`: 

![image](https://hackmd.io/_uploads/Bk49d06Vye.png)

So our graph is right. The description of `Bounties[3]` is saved in `0x55555555a310`, which is the metadata of `Bounties[1]`. So now we just need to view index 3 or index 2, it works anyway because now index 3 has `Bounty->active == 1`.

![image](https://hackmd.io/_uploads/S1CoYRTEyg.png)

![image](https://hackmd.io/_uploads/ryi3FCpNke.png)

So we leaked the heap base.
:::info
Some note: If you use debug or noaslr and see some garbage values like this 

![image](https://hackmd.io/_uploads/S1JW5Aa4yx.png)

Turn it off, just run locally and it will work.
:::
Now for stage 2, we need to create a chunk that can be placed in unsorted bin. 
The maximum size of tcache is 0x410

![image](https://hackmd.io/_uploads/ByJiqATN1g.png)

So we can create a 0x420 chunk size. Because we can modify the metadata of a chunk, so we can create some chunks, freed the first 2 chunks of them, so now if i malloc a `0x20` chunk, it will take place of first chunk's metadata for its and take second's metadata to hold the data of its description
First, for not to calculate too much, we create more a chunk to fit the metadata of `Bounties[0]`

![image](https://hackmd.io/_uploads/rkIF3CaEyx.png)

For now, i will not using NOASLR to calculate for avoiding that bug i talked before but it will not affect the solution. 
The `Bounties` will look like this 

![image](https://hackmd.io/_uploads/BJNBl10Ekl.png)

As you can see, the last index, which is our chunk used to modify metadata, has the same pointer to index 6: `0x000055e832f9d4c0`. So we want to modify the size of `Bounties[5]` (remember tcache is LIFO)

![image](https://hackmd.io/_uploads/BkRVWkCVJx.png)

![image](https://hackmd.io/_uploads/Hyj7bkREkl.png)

Now, if i delete index 5, it should work now. But i forget the `Bounties[5]->description` 's is still in tcache, this leads to double free: 

![image](https://hackmd.io/_uploads/Hy7uMkCE1g.png)

So maybe first, i need to create 2 more, to fill up the description of `Bounties[5] and Bounties[6]` 

![image](https://hackmd.io/_uploads/HJI8XBAEkl.png)

But i still got double free or corruption error: 

![image](https://hackmd.io/_uploads/rJEBQBR4Je.png)

So I tried to research some writeups, you can see the original [here](https://hackmd.io/@M_jkUUNmQBGqI26qqQamjg/Hkgda-3NJg)
So the idea is we can modify `Bounty->amount` to be our unsorted bin chunk's size, to create a fake chunk. Now, the `Bounty->description` pointer will be the fd pointer. 
First, we create some chunks to make up the fake chunk: 

![image](https://hackmd.io/_uploads/SyyrrrAVke.png)

![image](https://hackmd.io/_uploads/SkY9Hr0Nyl.png)

Remember, before that, the `Bounties[0]` is still in tcache, when we create out `Bounties[4]`, the metadata of index 0 will be used for creating metadata of index 4. The last chunk, we want to create a more fake chunk, in `0x563f8b450890`. This will split the fake chunk 1 to fake chunk 2. Our fake chunk 1 starts in offset `0x460` to offset `0x880`, so the size will be `0x880 - 0x460 = 0x430`, equals to the `Bounty->amount` (size of unsorted bin's fake chunk).
Now, we delete the `Bounties[2]` to bring the metadata of `Bounty[2]` then `Bounties[1]` to tcache

![image](https://hackmd.io/_uploads/Syd1dSANyl.png)

![image](https://hackmd.io/_uploads/S1Q-OrC4kl.png)

So now, if we malloc a `0x20` Bounty more, this will take the metadata of `Bounties[1]` for its metadata, then `Bounties[2]'s` for its description. Now we can modify the metadata of `Bounties[1]`:

![image](https://hackmd.io/_uploads/r17BeUAE1e.png)

This will modify the metadata of `Bounties[1]`, change the `Bounty->flag` to 1 so we can double free. 

![image](https://hackmd.io/_uploads/HkxZWIRN1g.png)

We delete the `Bounties[1]`. Its description, in `0x470`, should be in unsorted bin now. 

![image](https://hackmd.io/_uploads/H14vZUC4kx.png)

![image](https://hackmd.io/_uploads/rkedW8AVJe.png)

Nice! So now we just need to create a chunk more to bring it out unsorted bin. First, we create a `0x30` chunk, so now it will take out a `0x30` and a `0x40` in tcache

![image](https://hackmd.io/_uploads/S1Xxf80E1l.png)

This is the `Bounties[1]` original 

![image](https://hackmd.io/_uploads/rysBGIRVye.png)

Now, because `Bounties[2]` is still holding the metadata of `Bounties[1]` as its description, we can delete it, then malloc one more to fix the metadata of chunk 1, to points it to our fake chunk in unsorted bin, instead of its original description chunk

![image](https://hackmd.io/_uploads/HyjbmLCEkx.png)

it should give us the libc leak now: 

![image](https://hackmd.io/_uploads/H1DvX8RVyg.png)

Yayy! So now we have libc leak. Easy to recover its base. 

![image](https://hackmd.io/_uploads/HJj0XLC4yx.png)

Because from 2.34, they removed `__malloc_hook` and `__free_hook` to avoid their vulnerabilities

![image](https://hackmd.io/_uploads/By3NEUC4kl.png)

We now use a technique called [tcache poisoning](https://github.com/shellphish/how2heap/blob/master/glibc_2.35/tcache_poisoning.c) to change the return address `create()` to `system()`, so we can use `pop rdi` to pop a shell. 
First, we need to leak stack. Because now, `Bounties[2]` still holding the metadata of `Bounties[2]` (metadata) and metadata of `Bounties[1]` (description), we can free it then create another chunk contains stack leak address ( i will choose `libc.sym['environ']`) so when we view, it will print out the address of stack leak 

![image](https://hackmd.io/_uploads/rJzxFUC41l.png)

![image](https://hackmd.io/_uploads/BJB-YU0Nyg.png)

I set a breakpoint in create+515 to find the saved rbp address:

![image](https://hackmd.io/_uploads/B1CSivANkx.png)

So this will be in `0x00007ffec33491b0`
Next, i freed a chunk into tcache, next, malloc a chunk to fill out the metadata of recently chunk and the description of `Bounties[1]`

![image](https://hackmd.io/_uploads/SkYslu0Eyl.png)

So now the description in `Bounties[10]` is freed
Now, i freed `Bounties[6]`, which is in offset `0x500`. Then, i malloc one more to put out the metadata of `Bounties[6]`. 

![image](https://hackmd.io/_uploads/SyoxfdAEJx.png)

Why it doesn't take out the metadata of `Bounties[6]'s description'`? Because the description of `Bounties[6]` is 0x70, but we only malloc 0x60, then it will take from unsorted bin instead

![image](https://hackmd.io/_uploads/SJhQfdA41g.png)

You can see, unsorted bin lost 0x430 - 0x3f0 = 0x60.

![image](https://hackmd.io/_uploads/HkHszuRVkl.png)

Now the new chunk will have description in the first of unsorted bin 

![image](https://hackmd.io/_uploads/r1_xmd0Eye.png)

So now we can edit the fd and bk pointer of unsorted bin 

![image](https://hackmd.io/_uploads/rya8QO0VJx.png)

![image](https://hackmd.io/_uploads/HJMCm_RNyg.png)

Now we modified the chunk in 0x530. For pop a shell, we use ret2system
First, we create one more chunk to overwrite the return address of `create()`, then create a chunk with our ROPchain so it will trigger the `create()` to return a shell

![image](https://hackmd.io/_uploads/BkdASOCVJg.png)

My knowledge about heap is not good after all. So maybe somewhere is misunderstanding, please let me know
Final script: [solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/HTB_University_CTF_2024/dead_or_alive/solve.py)
