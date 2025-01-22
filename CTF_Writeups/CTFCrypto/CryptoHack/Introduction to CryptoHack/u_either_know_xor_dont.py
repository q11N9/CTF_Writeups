from pwn import *
c = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
# flag format: crypto{
flag1 = "crypto{"
flag2 = "}"
c_bytes = bytes.fromhex(c)
key = "".join(chr(ord(i) ^ j) for i, j in zip(flag1, c_bytes[:7]))
key += chr(c_bytes[len(c_bytes) - 1] ^ ord(flag2))
print("Key: " + key)
flag = ""
for i in range(len(c_bytes)): 
    flag += chr(ord(key[i % len(key)]) ^ c_bytes[i])
print("Flag: " + flag)
# crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}