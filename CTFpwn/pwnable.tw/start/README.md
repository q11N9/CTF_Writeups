We have given 2 functions when decompile file binary: `start()` and `exit()`

![image](https://hackmd.io/_uploads/ry-4Li1H1g.png)

![image](https://hackmd.io/_uploads/H1QBLi1SJl.png)

Maybe it's some assembly code. In 32 bits, `int 0x80` is the same as `syscall` in 64 bits to call the syswrite function. So we can execute shellcode here. 
We want to execute `execve('/bin/sh', 0,0)`. In gdb, the `_start` will be like this: 

![image](https://hackmd.io/_uploads/ryQ_vokHyl.png)

It use some `push` instruction to push parameter into stack. After that, it `mov al 0x4`, which is preparing to call syscall `write`: 

![image](https://hackmd.io/_uploads/HJYyuoJr1l.png)

to put in our input. 
When we run the binary file, we know that it's this string: 

![image](https://hackmd.io/_uploads/SkLiPiyH1x.png)

Next, it will add `esp + 0x14` so we know that is the return address

![image](https://hackmd.io/_uploads/rkcvcikHyg.png)

You can see the return address is in `0xffffd5f8 = esp+0x14`. Because there is no limit for our input so we can overflow the return address, we can return to our input so we can leak out the `saved rbp`. After that, we can input our shellcode to execute `execve('/bin/sh', 0,0)`.
Script: [solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/pwnable.tw/start/solve.py)
