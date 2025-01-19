We have given a [libc_32.so.6](https://pwnable.tw/static/libc/libc_32.so.6) and binary [file](https://pwnable.tw/static/chall/spirited_away). Patched it, we know that this is libc 2.23

![image](https://hackmd.io/_uploads/SyVG2xNI1l.png)

Decompile binary file to see what's inside: 
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  puts("Thanks for watching Spirited Away!");
  puts("Please leave some comments to help us improve our next movie!");
  fflush(stdout);
  return survey();
}
```
`survey()` function: 
```c
int survey()
{
  char announce[56]; // [esp+10h] [ebp-E8h] BYREF
  int size60; // [esp+48h] [ebp-B0h]
  int size80; // [esp+4Ch] [ebp-ACh]
  char comment[80]; // [esp+50h] [ebp-A8h] BYREF
  int age; // [esp+A0h] [ebp-58h] BYREF
  const char *name; // [esp+A4h] [ebp-54h]
  char reason[80]; // [esp+A8h] [ebp-50h] BYREF

  size60 = 60;
  size80 = 80;
LABEL_2:
  memset(comment, 0, sizeof(comment));
  name = (const char *)malloc(0x3C);
  printf("\nPlease enter your name: ");
  fflush(stdout);
  read(0, name, size60);
  printf("Please enter your age: ");
  fflush(stdout);
  __isoc99_scanf("%d", &age);
  printf("Why did you came to see this movie? ");
  fflush(stdout);
  read(0, reason, size80);
  fflush(stdout);
  printf("Please enter your comment: ");
  fflush(stdout);
  read(0, comment, size60);
  ++cnt;
  printf("Name: %s\n", name);
  printf("Age: %d\n", age);
  printf("Reason: %s\n", reason);
  printf("Comment: %s\n\n", comment);
  fflush(stdout);
  sprintf(announce, "%d comment so far. We will review them as soon as we can", cnt);
  puts(announce);
  puts(&unk_8048A81);
  fflush(stdout);
  if ( cnt > 199 )
  {
    puts("200 comments is enough!");
    fflush(stdout);
    exit(0);
  }
  while ( 1 )
  {
    printf("Would you like to leave another comment? <y/n>: ");
    fflush(stdout);
    read(0, &choice, 3);
    if ( choice == 'Y' || choice == 'y' )
    {
      free(name);
      goto LABEL_2;
    }
    if ( choice == 'N' || choice == 'n' )
      break;
    puts("Wrong choice.");
    fflush(stdout);
  }
  puts("Bye!");
  return fflush(stdout);
}
```

A survey program. It reads our input with parameter `name, age, reason, comment`. Then it will print out a announcement for us to show how many comments was     sent. If we countinue to take a survey, it will free our name. 
The first thing i notice is why `comment` is initialized with the size 80, but they only read with `size60`? And it uses `sprintf` to copy the announcement to `announce`. But `announce` has static size, which is 56. But the length of the string in `sprintf` is dynamic, depends on the length of `cnt`. In start, that string has 55-char length

![image](https://hackmd.io/_uploads/rJL1kZVLkx.png)

What if we input 10 comments? 100 comments? Our `annouce`'s size will be 56 then 57. But right under it is `size60`, which is the size of `name` and `comment[]`

![image](https://hackmd.io/_uploads/SJ40kbVUke.png)

![image](https://hackmd.io/_uploads/H1ZXeZEUkg.png)

So it we input 100 comments, it will overflow that last character of that string - character `n`. In ascii, it is bigger than 60

![image](https://hackmd.io/_uploads/HJQIKWVUJe.png)

So we can overflow the value of `name`, make it points to a fake chunk so we can control that chunk. Why we can't control the chunk that program give us(That 0x3c)? Because of heap consolidation, if there is no chunk after it, it will consolide with top chunk, not going to bins so we cannot control it. 
But first, we must leak libc. This program uses `printf` to print out those values. But `printf` only stop if it meets null byte. So we can leak it through `name`, `age`,`comment`.
This is how stack was:

![image](https://hackmd.io/_uploads/rJpqxn4Lke.png)

![image](https://hackmd.io/_uploads/r1sigh4Iyx.png)


You can see the addresses of our variables: 

![image](https://hackmd.io/_uploads/H1hW-3VIke.png)

Look at the stack, we must use `reason` to leak out data. Our `reason` is in `0xfff2a958` currently. The first value seems like a stack address. Under it, in `0xfff2a96c`, there is a libc address. So my idea is: 
- Leak stack and libc. 
- Overflow `size60`, change its size to `0x6e = n`. 
- Overflow the value of `*name`, change it to point to our fake chunk
- Put our fake chunk into bin. 
- Put out our fake chunk, change its content to execute `system('/bin/sh')` to get shell. 

Leak stack: 

![image](https://hackmd.io/_uploads/HkkkX3V8yg.png)

![image](https://hackmd.io/_uploads/BycB73VUJx.png)

Leak libc: 

![image](https://hackmd.io/_uploads/ByL6VhEIyl.png)


![image](https://hackmd.io/_uploads/HkPAN24IJx.png)


Now we need to overflow `size60` by increasing our `cnt`: 

![image](https://hackmd.io/_uploads/B1ui934Ikx.png)

For some reason, after 10 comments, my input cannot be passed normally so i must change how i send data. 
Now `size60`, in `ebp - 0xb0`, should be `0x6e`:

![image](https://hackmd.io/_uploads/r1IMohVUkl.png)

In `0xffd73c64`, it is `size60`, under it is `size80`.

Because we can use `comment` to overflow the address of `*name`, point it to a fake chunk. `reason` is a good space for us to create a fake chunk. 

Our fake chunk will have the size `0x40`, because they initialize the `name` chunk with total size `0x40`

![image](https://hackmd.io/_uploads/HyjtTyBIkg.png)

In the process of overwrite `*name`, i had a problem. My `stack_leak`'s offset before does not static. Because i want to point it to a `$ebp - 0x50 - 0x8` (0x8 for metadata of our fake chunk), so i calculated some cases and saw that it is not static:
Case 1:

![image](https://hackmd.io/_uploads/ryr8CJr8yg.png)

![image](https://hackmd.io/_uploads/Bk5pRJr8yg.png)

Case 2:

![image](https://hackmd.io/_uploads/BkU1JxBU1x.png)

![image](https://hackmd.io/_uploads/Syg7yeBLkl.png)

So i must rewrite the leak stack part to correct it.

![image](https://hackmd.io/_uploads/BkHpeerIkl.png)

![image](https://hackmd.io/_uploads/r10w-eSL1x.png)

![image](https://hackmd.io/_uploads/Hyv5beB8kx.png)


Seems it is right now. 

![image](https://hackmd.io/_uploads/Bk0nXer8Jl.png)

Now we can use `name` to modify the return address. Because of the size of `reason`, only 80, but now we use `name` to point it to `reason`, so we can overflow saved ebp (`0x6e` is much bigger than 80)

![image](https://hackmd.io/_uploads/BJfaNgrIkg.png)

![image](https://hackmd.io/_uploads/H1WnNgrU1g.png)

Offset from input `name` to return address is `0x4c`

![image](https://hackmd.io/_uploads/ryDmHeSIJg.png)

Now we just need to use ret2system. But there is a problem. Because the address of libc leak is above stack leak, so i leaked libc after stack, which i was use payload to overwrite the old libc leak (the puts and \_IO\_file\_sync)

![image](https://hackmd.io/_uploads/rkyzDgrLkg.png)

Just need to change the order a little bit

![image](https://hackmd.io/_uploads/r1xXDDeHIJg.png)

And overwrite saved ebp

![image](https://hackmd.io/_uploads/SJS5DxBLkg.png)

We get the shell! 

![image](https://hackmd.io/_uploads/rye0vgSI1g.png)

When i run remotely, it doesn't work properly in leaking libc, so i must change a little bit.
Script: [solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/pwnable.tw/SpiritedAway/solve.py)
