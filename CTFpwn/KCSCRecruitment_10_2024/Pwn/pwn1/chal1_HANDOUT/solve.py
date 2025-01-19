#!/usr/bin/env python3

from pwn import *

exe = ELF("./chal1")

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 13775)

    return r


context.binary = exe
def main():
	r = conn()
	
	
	pause()
	r.interactive()

if __name__ == "__main__":
    main()
