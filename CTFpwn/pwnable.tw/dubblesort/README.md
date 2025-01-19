This time, we get libc file to patch. 

![image](https://hackmd.io/_uploads/SyAQpFgrkx.png)

Decompile binary file: 
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  int **v4; // edi
  unsigned int i; // esi
  unsigned int j; // esi
  int result; // eax
  unsigned int amount; // [esp+18h] [ebp-74h] BYREF
  int num_arr[8]; // [esp+1Ch] [ebp-70h] BYREF
  int name; // [esp+3Ch] [ebp-50h] BYREF
  unsigned int v11; // [esp+7Ch] [ebp-10h]

  v11 = __readgsdword(0x14u);
  sub_8B5();
  __printf_chk(1, "What your name :");
  read(0, &name, 64);
  __printf_chk(1, "Hello %s,How many numbers do you what to sort :");
  __isoc99_scanf("%u", &amount);
  v3 = amount;
  if ( amount )
  {
    v4 = (int **)num_arr;
    for ( i = 0; i < amount; ++i )
    {
      __printf_chk(1, "Enter the %d number : ");
      fflush(stdout);
      __isoc99_scanf("%u", v4);
      v3 = amount;
      ++v4;
    }
  }
  sort(num_arr, v3);
  puts("Result :");
  if ( amount )
  {
    for ( j = 0; j < amount; ++j )
      __printf_chk(1, "%u ");
  }
  result = 0;
  if ( __readgsdword(0x14u) != v11 )
    return sub_BA0();
  return result;
}
```

It first read our name, then let us input an array. Then it will sort our array. But wait, our array's size is only 8. So we have a buffer overflow here. Next, in `sort()` function: 

```c
unsigned int __cdecl sort(unsigned int *num_arr, int size)
{
  int v2; // ecx
  int i; // edi
  unsigned int v4; // edx
  unsigned int v5; // esi
  unsigned int *numPtr; // eax
  unsigned int result; // eax
  unsigned int v8; // [esp+1Ch] [ebp-20h]

  v8 = __readgsdword(0x14u);
  puts("Processing......");
  sleep(1);
  if ( size != 1 )
  {
    v2 = size - 2;
    for ( i = (int)&num_arr[size - 1]; ; i -= 4 )
    {
      if ( v2 != -1 )
      {
        numPtr = num_arr;
        do
        {
          v4 = *numPtr;
          v5 = numPtr[1];
          if ( *numPtr > v5 )
          {
            *numPtr = v5;
            numPtr[1] = v4;
          }
          ++numPtr;
        }
        while ( (unsigned int *)i != numPtr );
        if ( !v2 )
          break;
      }
      --v2;
    }
  }
  result = __readgsdword(0x14u) ^ v8;
  if ( result )
    return sub_BA0();
  return result;
}
```
It seems fine.
When i run the file and input name, something strange appears. I thought it was some mistake of my computer but it comes from a bug of program: 

![image](https://hackmd.io/_uploads/SyOXl9lBJe.png)

That strange string after or name is some leaking data. Checking in gdb: 

![image](https://hackmd.io/_uploads/ryKueqgHke.png)

I set breakpoint in `main+116` to see where is our string. 

![image](https://hackmd.io/_uploads/HyqUW5xr1x.png)

![image](https://hackmd.io/_uploads/SJE_Z9erkx.png)

So this is the leak data. Why? Because `printf()` only stop when scan to byte null. But after `read()` name from input, the program did not nulldify the last character, so we can leak libc address by using this bug. 

![image](https://hackmd.io/_uploads/SkDsQclHkg.png)

![image](https://hackmd.io/_uploads/rkqpXqlrkl.png)

![image](https://hackmd.io/_uploads/SJ_0QqeHkx.png)

So now we have libc and /bin/sh address. 
Because there is a buffer overflow bug here, we can overwrite return address to system and pop a shell. But there is canary here, in `ebp-0x10`:

![image](https://hackmd.io/_uploads/HysD49lryx.png)

And our `num_arr` starts in `ebp-0x70`

![image](https://hackmd.io/_uploads/rJio4cgSJg.png)

So the offset to canary will be 25 or index 24.

![image](https://hackmd.io/_uploads/SyrbHqgryg.png)

About the size we want to input, first, 25 to canary + 8 more to return address + 2 more for return address of system() and system's parameter = 35
And also, we can payload canary by inputting `+` or `-`
Script: [solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/pwnable.tw/dubblesort/solve.py)
