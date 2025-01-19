We have libc and file binary. Decompile binary file: 
```c
void __cdecl __noreturn main()
{
  int choice; // eax
  int v1; // [esp-Ch] [ebp-24h]
  int v2; // [esp-8h] [ebp-20h]
  int v3; // [esp-4h] [ebp-1Ch]
  char v4[4]; // [esp+8h] [ebp-10h] BYREF
  unsigned int v5; // [esp+Ch] [ebp-Ch]

  v5 = __readgsdword(0x14u);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  while ( 1 )
  {
    while ( 1 )
    {
      menu();
      read(0, v4, 4);
      choice = atoi(v4);
      if ( choice != 2 )
        break;
      delete_note();
    }
    if ( choice > 2 )
    {
      if ( choice == 3 )
      {
        print_note();
      }
      else
      {
        if ( choice == 4 )
          exit(0, v1, v2, v3);
LABEL_13:
        puts("Invalid choice");
      }
    }
    else
    {
      if ( choice != 1 )
        goto LABEL_13;
      add_note();
    }
  }
}
```

![image](https://hackmd.io/_uploads/SJrwtqxrke.png)

An add,delete and view note menu. 
`add_note()`: 
```c
unsigned int add_note()
{
  Note *v0; // ebx
  int v2; // [esp-Ch] [ebp-34h]
  int v3; // [esp-Ch] [ebp-34h]
  int v4; // [esp-8h] [ebp-30h]
  int v5; // [esp-8h] [ebp-30h]
  int v6; // [esp-4h] [ebp-2Ch]
  int i; // [esp+Ch] [ebp-1Ch]
  int size; // [esp+10h] [ebp-18h]
  char v9[8]; // [esp+14h] [ebp-14h] BYREF
  unsigned int v10; // [esp+1Ch] [ebp-Ch]

  v10 = __readgsdword(0x14u);
  if ( limit <= 5 )
  {
    for ( i = 0; i <= 4; ++i )
    {
      if ( !noteArr[i] )
      {
        noteArr[i] = (Note *)malloc(8);
        if ( !noteArr[i] )
        {
          puts("Alloca Error");
          exit(-1, v2, v4, v6);
        }
        noteArr[i]->print_func = printFunction;
        printf("Note size :");
        read(0, v9, 8);
        size = atoi(v9);
        v0 = noteArr[i];
        v0->content = (char *)malloc(size);
        if ( !noteArr[i]->content )
        {
          puts("Alloca Error");
          exit(-1, v3, v5, v6);
        }
        printf("Content :");
        read(0, noteArr[i]->content, size);
        puts("Success !");
        ++limit;
        return __readgsdword(0x14u) ^ v10;
      }
    }
  }
  else
  {
    puts("Full");
  }
  return __readgsdword(0x14u) ^ v10;
}
```
Struct of a `Note`: 

![image](https://hackmd.io/_uploads/B1byJigHJl.png)

We can malloc maximum 5 notes, each note has size and content. Nothing special here, just create. 

`delete_note()`:
```c
unsigned int delete_note()
{
  int v1; // [esp-Ch] [ebp-24h]
  int v2; // [esp-8h] [ebp-20h]
  int v3; // [esp-4h] [ebp-1Ch]
  int v4; // [esp+4h] [ebp-14h]
  char v5[4]; // [esp+8h] [ebp-10h] BYREF
  unsigned int v6; // [esp+Ch] [ebp-Ch]

  v6 = __readgsdword(0x14u);
  printf("Index :");
  read(0, v5, 4);
  v4 = atoi(v5);
  if ( v4 < 0 || v4 >= limit )
  {
    puts("Out of bound!");
    _exit(0, v1, v2, v3);
  }
  if ( noteArr[v4] )
  {
    free(noteArr[v4]->content);
    free(noteArr[v4]);
    puts("Success");
  }
  return __readgsdword(0x14u) ^ v6;
}
```
It first free the content then free the chunk contains note wanted to delete. But there is still pointer to that chunk in `noteArr`.
`print_note()`:
```c
unsigned int print_note()
{
  int v1; // [esp-Ch] [ebp-24h]
  int v2; // [esp-8h] [ebp-20h]
  int v3; // [esp-4h] [ebp-1Ch]
  int v4; // [esp+4h] [ebp-14h]
  char v5[4]; // [esp+8h] [ebp-10h] BYREF
  unsigned int v6; // [esp+Ch] [ebp-Ch]

  v6 = __readgsdword(0x14u);
  printf("Index :");
  read(0, v5, 4);
  v4 = atoi(v5);
  if ( v4 < 0 || v4 >= limit )
  {
    puts("Out of bound!");
    _exit(0, v1, v2, v3);
  }
  if ( noteArr[v4] )
    ((void (__cdecl *)(Note *))noteArr[v4]->print_func)(noteArr[v4]);
  return __readgsdword(0x14u) ^ v6;
}
```
Just print out the note. 

Our target is still leaking the libc first. Because we have libc here, we just need to print out the value of puts.got so we can leak the libc. 
And there is a trick here. Because it always has a chunk for size, which is `0x10` (in 32bit, metadata of a chunk has the size 0x8):

![image](https://hackmd.io/_uploads/H1k5n5eByg.png)

![image](https://hackmd.io/_uploads/H1w9kigHyl.png)

We can malloc 2 notes first, free them, and a note with the size `0x8`, so the third note will use the metadata of 2 previous note as its metadata and content. So we can use that trick to modify metadata of a note, overwrite the `print_func` to `system()` then printout the content, we will get the shell. 
First, malloc 2 chunk and free it

![image](https://hackmd.io/_uploads/BkHheigrJe.png)

The heap before free will be look like this: 

![image](https://hackmd.io/_uploads/SycaxjxHyx.png)

The first 4 bytes is print function pointer, then the content pointer. 
Now free them: 

![image](https://hackmd.io/_uploads/Hy8qMjxr1l.png)

So now if i malloc a `0x8` note, it will take out 2 chunks in fastbin index 0: 

![image](https://hackmd.io/_uploads/HysnMolHye.png)

![image](https://hackmd.io/_uploads/ByRCGilBJe.png)

You can see that the metadata of index 0 has been modified.
We can modify the `print_func` to puts address to printout the puts.got

![image](https://hackmd.io/_uploads/S1B_QsgS1l.png)

Now the heap will be like this: 

![image](https://hackmd.io/_uploads/ByZh7oxBJl.png)

![image](https://hackmd.io/_uploads/HyxyNjxrJx.png)

So if we call to print out note 0, it should give us the libc leak. 

![image](https://hackmd.io/_uploads/S1tMEoeSkl.png)

So with the same method, we can modify `print_func` to `system()` and the pointer to content, modify it to `;sh` which is the parameter of `system()`

![image](https://hackmd.io/_uploads/rJ8IEolBkg.png)

Result: 

![image](https://hackmd.io/_uploads/BJADVixSyl.png)

Script: [solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/pwnable.tw/hacknote/solve.py)
