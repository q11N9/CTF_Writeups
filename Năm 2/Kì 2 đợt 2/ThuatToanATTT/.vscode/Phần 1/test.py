import random
import string
def decode(cipher, key):
    flag = ""
    xored = bytes.fromhex(cipher).decode()
    for i in range(0, len(xored)):
        flag += chr(ord(xored[i]) ^ ord(key[i%len(key)]))
    return flag 
res = ''.join(random.choices(string.ascii_letters + string.digits, k = 5))
key = str(res)
print(key)
cipher = input("Nhap cipher: ")
flag = decode(cipher, key)
while(flag[:4] != "THM{" or flag[len(flag) - 1] != "}"):
    res = ''.join(random.choices(string.ascii_letters + string.digits, k = 5))
    key = str(res)
    flag = decode(cipher, key)
print(key)   
flag = decode(cipher, key)
print(flag)