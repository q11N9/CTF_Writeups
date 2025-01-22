from pwn import *
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_X_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_X_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_X_KEY1_X_KEY3_X_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

k1 = bytes.fromhex(KEY1)
k2_x_k1 = bytes.fromhex(KEY2_X_KEY1)
k2_x_k3 = bytes.fromhex(KEY2_X_KEY3)
flag_x_k1_x_k3_x_k2 = bytes.fromhex(FLAG_X_KEY1_X_KEY3_X_KEY2)

k2 = bytes(i ^ j for i, j in zip(k1, k2_x_k1))
k3 = bytes(i ^ j for i, j in zip(k2_x_k3, k2))
res1 = bytes(i ^ j for i, j in zip(flag_x_k1_x_k3_x_k2, k2))
res2 = bytes(i ^ j for i, j in zip(res1, k3))
res3 = bytes(i ^ j for i, j in zip(res2, k1))

flag = "".join(chr(c) for c in res3)
print("Flag: " + flag)
# crypto{x0r_i5_ass0c1at1v3}