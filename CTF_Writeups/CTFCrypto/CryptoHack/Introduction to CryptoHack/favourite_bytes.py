from pwn import *
c = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
c_bytes = bytes.fromhex(c)
for i in range(100):
    res = "".join(chr(o ^ i) for o in c_bytes)
    if res[:7] == "crypto{":
        print("Flag: " + res)
# crypto{0x10_15_my_f4v0ur173_by7e}