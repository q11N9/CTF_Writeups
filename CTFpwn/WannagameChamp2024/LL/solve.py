#!/usr/bin/env python3

from pwn import *

exe = ELF("./ll_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()
    ######################
    #puts("1. Add number array");
    # puts("2. Delete number array");
    # puts("3. View number array");
    # puts("4. Edit number array");
    # puts("5. Add name array");
    # puts("6. Delete name array");
    # puts("7. Exit");
    # printf("Your choice: ");
    ######################
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
