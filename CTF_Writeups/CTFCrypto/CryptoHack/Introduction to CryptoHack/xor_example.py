from pwn import *
c = "label"
res = "".join(chr(ord(char)^13) for char in c)
print(res)
# crypto{aloha}