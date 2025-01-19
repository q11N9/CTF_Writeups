We have a binary file. And the hint is send a shellcode with only `open, read, write` syscall. 

![image](https://hackmd.io/_uploads/HJaanH_Qkg.png)

![image](https://hackmd.io/_uploads/rJ402SOXyg.png)

So our idea is push the name of file into stack, which is `rsp` register. Then open it, read it and write it to our screen. 

For pushing directory to stack: 

```c!
push 0x0
push 0x67616c66	
push 0x2f77726f	
push 0x2f656d6f	
push 0x682f2f2f
```
because this is 32 bit program, so i only write 4 bytes each time, with little endian order. And lastly, we must push the null byte in the end

For registers to open, read, write, you can read in [here](https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86-32_bit), in x86 section. 
Script: [solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/pwnable.tw/orw/solve.py)
Flag: ```FLAG{sh3llc0ding_w1th_op3n_r34d_writ3}```
