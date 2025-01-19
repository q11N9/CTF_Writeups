We decompile the binary file: 

![image](https://hackmd.io/_uploads/BJmSqdlryx.png)

The code is made for avoiding us to read clearly. But we still could find the start. 
```c
// positive sp value has been detected, the output may be wrong!
void __fastcall __noreturn start(__int64 a1, __int64 a2, int a3)
{
  __int64 v3; // rax
  int v4; // esi
  __int64 v5; // [rsp-8h] [rbp-8h] BYREF
  void *retaddr; // [rsp+0h] [rbp+0h] BYREF

  v4 = v5;
  v5 = v3;
  sub_401EB0(
    (unsigned int)sub_401B6D,
    v4,
    (unsigned int)&retaddr,
    (unsigned int)sub_4028D0,
    (unsigned int)sub_402960,
    a3,
    (__int64)&v5);
  __halt();
}
```
`sub_401EB0` maybe some control function: 
```c
// write access to const memory has been detected, the output may be wrong!
void __fastcall __noreturn sub_401EB0(
        __int64 (__fastcall *a1)(_QWORD, __int64, __int64),
        unsigned int a2,
        __int64 a3,
        void (__fastcall *a4)(_QWORD, __int64, __int64),
        __int64 a5,
        __int64 a6,
        __int64 a7)
{
  __int64 v10; // rdi
  __int64 v11; // rax
  int v17; // eax
  __int64 (__fastcall ***i)(); // rbx
  __int64 v19; // rax
  __int64 *v20; // r14
  int v31; // eax
  unsigned __int64 v32; // rax
  unsigned int v33; // eax
  signed __int64 v34; // rax
  const char *v35; // rax
  int v36; // eax
  int v47; // eax
  int v48; // eax
  int v51; // [rsp+28h] [rbp-D0h] BYREF
  int v52; // [rsp+2Ch] [rbp-CCh] BYREF
  int v53; // [rsp+30h] [rbp-C8h] BYREF
  unsigned int v54; // [rsp+34h] [rbp-C4h] BYREF
  char v55[4]; // [rsp+38h] [rbp-C0h] BYREF
  char v56[4]; // [rsp+3Ch] [rbp-BCh] BYREF
  char v57[8]; // [rsp+40h] [rbp-B8h] BYREF
  __int64 v58; // [rsp+48h] [rbp-B0h] BYREF
  __int64 v59; // [rsp+50h] [rbp-A8h] BYREF
  __int64 v60; // [rsp+58h] [rbp-A0h] BYREF
  char v61[72]; // [rsp+60h] [rbp-98h] BYREF
  unsigned __int64 v62; // [rsp+A8h] [rbp-50h]
  unsigned __int64 v63; // [rsp+B0h] [rbp-48h]

  dword_4B8798 = 0;
  nullsub_1();
  v10 = a3 + 8LL * (int)a2 + 8;
  qword_4B9DA8 = v10;
  qword_4B6AB0 = a7;
  do
    v10 += 8LL;
  while ( *(_QWORD *)(v10 - 8) );
  sub_44AC60();
  if ( !qword_4BA8B8 && &dword_400000 )
  {
    if ( *((_WORD *)&dword_400000 + 27) != 56 )
      sub_402B10("__ehdr_start.e_phentsize == sizeof *GL(dl_phdr)", "../csu/libc-start.c", 180LL, "__libc_start_main");
    v11 = *((unsigned __int16 *)&dword_400000 + 28);
    qword_4BA8B8 = (__int64)&dword_400000 + *((_QWORD *)&dword_400000 + 4);
    qword_4BA8F0 = v11;
  }
  sub_44B870();
  sub_44A610(qword_4B9DA8);
  _RAX = 0LL;
  v51 = 0;
  __asm { cpuid }
  v52 = 0;
  dword_4B9DE4 = _RAX;
  if ( (_DWORD)_RBX == 1970169159 && (_DWORD)_RCX == 1818588270 )
  {
    if ( (_DWORD)_RDX != 1231384169 )
    {
LABEL_10:
      sub_401C50(0LL, 0LL, 0LL, 0LL);
      v17 = 3;
      goto LABEL_11;
    }
    sub_401C50(&v51, &v52, &v53, &v54);
    _RAX = 0x80000000LL;
    __asm { cpuid }
    if ( (unsigned int)_RAX > 0x80000000 )
    {
      _RAX = 2147483649LL;
      __asm { cpuid }
      dword_4B9E08 = _RAX;
      dword_4B9E0C = _RBX;
      dword_4B9E10 = _RCX;
      dword_4B9E14 = _RDX;
    }
    if ( v51 == 6 )
    {
      v52 += v53;
      switch ( v52 )
      {
        case 26:
        case 30:
        case 31:
        case 37:
        case 44:
        case 46:
        case 47:
          goto LABEL_79;
        case 28:
        case 38:
          dword_4B9E2C |= 4u;
          break;
        case 55:
        case 74:
        case 76:
        case 77:
        case 87:
        case 90:
        case 92:
        case 93:
        case 95:
          dword_4B9E2C |= 0x40230u;
          break;
        case 60:
        case 69:
        case 70:
          goto LABEL_75;
        case 63:
          if ( v54 <= 3 )
LABEL_75:
            dword_4B9DFC &= ~0x800u;
          break;
        default:
          if ( (dword_4B9DF0 & 0x10000000) != 0 )
LABEL_79:
            dword_4B9E2C |= 0x40031u;
          break;
      }
    }
    v47 = dword_4B9E2C | 0x100000;
    if ( (dword_4B9DFC & 0x8000000) != 0 )
      v47 = dword_4B9E2C | 0x20000;
    dword_4B9E2C = v47;
    v17 = 1;
  }
  else
  {
    if ( (_DWORD)_RCX != 1145913699 || (_DWORD)_RBX != 1752462657 || (_DWORD)_RDX != 1769238117 )
      goto LABEL_10;
    sub_401C50(&v51, &v52, v55, v56);
    _RAX = 0x80000000LL;
    __asm { cpuid }
    if ( (unsigned int)_RAX > 0x80000000 )
    {
      _RAX = 2147483649LL;
      __asm { cpuid }
      dword_4B9E08 = _RAX;
      dword_4B9E0C = _RBX;
      dword_4B9E10 = _RCX;
      dword_4B9E14 = _RDX;
    }
    v31 = dword_4B9E2C;
    if ( (dword_4B9E2C & 0x40) != 0 && (dword_4B9E10 & 0x10000) != 0 )
    {
      BYTE1(v31) = BYTE1(dword_4B9E2C) | 1;
      dword_4B9E2C = v31;
    }
    if ( v51 == 21 && (unsigned int)(v52 - 96) <= 0x1F )
    {
      v48 = dword_4B9E2C;
      BYTE1(v48) = BYTE1(dword_4B9E2C) & 0xF7;
      dword_4B9E2C = v48 | 0x12;
    }
    v17 = 2;
  }
LABEL_11:
  if ( (dword_4B9DF4 & 0x100) != 0 )
    dword_4B9E2C |= 0x4000u;
  if ( (dword_4B9DF4 & 0x8000) != 0 )
    dword_4B9E2C |= 0x8000u;
  dword_4B9DE0 = v17;
  dword_4B9E18 = v51;
  dword_4B9E1C = v52;
  sub_44ABE0(0LL, v57, sub_44B900);
  sub_44ABE0(13LL, &v58, 0LL);
  qword_4B9E40 = v58;
  sub_44ABE0(21LL, &v59, 0LL);
  qword_4B9E30 = v59;
  sub_44ABE0(14LL, &v60, 0LL);
  qword_4B9DC8 = 2LL;
  qword_4B9E38 = v60;
  if ( dword_4B9DE0 != 1 )
  {
LABEL_16:
    for ( i = &off_400248; (unsigned __int64)i < 0x400470; i += 3 )
    {
      v20 = (__int64 *)*i;
      if ( *((_DWORD *)i + 2) != 37 )
        sub_413540("unexpected reloc type in static binary");
      v19 = ((__int64 (*)(void))i[2])();
      *v20 = v19;
    }
    sub_402690();
    v32 = *(_QWORD *)qword_4B6AA0;
    LOBYTE(v32) = 0;
    __writefsqword(0x28u, v32);
    if ( !dword_4B8798 )
    {
      v36 = sub_44C590();
      if ( v36 < 0 )
        sub_413540("FATAL: cannot determine kernel version\n");
      if ( !dword_4BA910 || dword_4BA910 > (unsigned int)v36 )
        dword_4BA910 = v36;
      if ( v36 <= 197119 )
        sub_413540("FATAL: kernel too old\n");
    }
...
```
In `sub_401b6d`:
```c
__int64 sub_401B6D()
{
  __int64 result; // rax
  char *v1; // [rsp+8h] [rbp-28h]
  char buf[24]; // [rsp+10h] [rbp-20h] BYREF
  unsigned __int64 v3; // [rsp+28h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  result = (unsigned __int8)++byte_4B9330;
  if ( byte_4B9330 == 1 )
  {
    sub_446EC0(1u, "addr:", 5uLL);
    sub_446E20(0, buf, 0x18uLL);
    v1 = (char *)(int)sub_40EE70(buf);
    sub_446EC0(1u, "data:", 5uLL);
    sub_446E20(0, v1, 0x18uLL);
    result = 0LL;
  }
  if ( __readfsqword(0x28u) != v3 )
    sub_44A3E0();
  return result;
}
```
So this maybe our main function. If we run the binary file: 

![image](https://hackmd.io/_uploads/HJd9iOlByx.png)

But input into, we don't have anything much. You can see the position of `data` and `addr`, it is in `rbp-0x20` and `rbp-0x28`. So maybe the program will let us change the data in the input address.
So what do we do now? I thought we can use ROP to pop a shell, but our payload is limited in `0x18`. So we must do something to return to our main function. 
But our stack is using dynamical address 

![image](https://hackmd.io/_uploads/HyHO0deBkx.png)

![image](https://hackmd.io/_uploads/BynhA_eBke.png)

And we cannot leak any data, so we cannot overwrite the `ret` address.
I read some writeup and they used overwrite `.fini_array`. 
:::info
`.fini_array` is a binary section, contains necessary deconstructor functions when function `main()` return. Opposite from `.fini_array`, `.init_array` contains constructor functions. 
:::
`.fini_array` has 2 entries: 
- `do_global_dtors_aux`: destructors used when `.fini_array` is not recognized. 
- `foo_destructor`: the address of destructor function. 
It will execute `foo_destructor` first, then `.fini_array`.

![image](https://hackmd.io/_uploads/S1uY8Ferkg.png)

You can read more in [here](https://blog.k3170makan.com/2018/10/introduction-to-elf-format-part-v.html)

Our idea is to overwrite `foo_destructor` to `main()` so we can control the flow. 
We know the address of `main()` because no PIE enabled. 
For `.fini_array`, because IDA is kinda confusing, i will use ghidra to decompile. 

![image](https://hackmd.io/_uploads/rkhPXFgBJe.png)

so `.fini_array` address is `0x401b00`. Or you can find it in the `entry()`:

![image](https://hackmd.io/_uploads/BkqsXKeS1x.png)

The `0x402960` is the address of `__libc_csu_fini`. Go into it: 

![image](https://hackmd.io/_uploads/S1oe4FxHyl.png)

We also get the address of `.fini_array` too. 
Overwrite `foo_destructor`: 

![image](https://hackmd.io/_uploads/HkwUVtgB1g.png)

so now the program will return to main. 

![image](https://hackmd.io/_uploads/SJD6VKgrye.png)

Now we want to find some gadget to execute `execve('/bin/sh', 0, 0)`:

![image](https://hackmd.io/_uploads/r1gmBKeBkl.png)

![image](https://hackmd.io/_uploads/HJaSSYeHJe.png)

![image](https://hackmd.io/_uploads/r1nUSKeHkx.png)

![image](https://hackmd.io/_uploads/rJvvrYgSyg.png)

![image](https://hackmd.io/_uploads/BySdrYxHJe.png)

And also, a `rw_section` for us to write `/bin/sh`. 
We can find it in rw section of binary: 

![image](https://hackmd.io/_uploads/ByfTDFxr1x.png)

This space is enough for us to write `/bin/sh\0`.
 And to read, we need to find the address of `read()` function too. 
 
 ![image](https://hackmd.io/_uploads/ry8rOFgBJe.png)
 
`read()` function maybe in `0x446e20`
After retrun, you can see `rbp` is points to `.fini_array`: 

![image](https://hackmd.io/_uploads/Hk0EqYgrkl.png)

so our return address will be `.fini_array + 0x8`. After that is our payload, from `.fini_array + 0x10`. 
Our payload will be like this: 

![image](https://hackmd.io/_uploads/SksO5Klrkx.png)

First, it prepares registers for `read()` syscall 

![image](https://hackmd.io/_uploads/HJ3TcFeryx.png)

Then after that, it will call `execve()`. 
Next, we will overwrite `.fini_array+0x10` to our payload. Because we can only input `0x18` for `data` each time, so we must make a loop: 

![image](https://hackmd.io/_uploads/SJ3csYeHke.png)

Next, we want to return our program. 

![image](https://hackmd.io/_uploads/B1kJ2KeH1e.png)

We can find the `leave_ret` and `ret` here. 
Script: [[solve.py](https://github.com/q11N9/CTF_Writeups/blob/main/CTFpwn/pwnable.tw/3x17/solve.py)]

![image](https://hackmd.io/_uploads/HkCgTKgr1l.png)
