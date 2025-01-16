import random
import math
def BinaryInversionInFp(p, a):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1 and v != 1 : 
        while u % 2 == 0:
            u = int(u/2)
            if x1 % 2 == 0: 
                x1 = int(x1 / 2)
            else:
                x1 = int((x1 + p) / 2)
        while v % 2 == 0: 
            v = v / 2
            if x2 % 2 == 0:
                x2 = int(x2/2)
            else: 
                x2 = int((x2 + p) / 2)
        if u >= v: 
            u = u - v
            x1 = x1 - x2
        else:
            v = v - u
            x2 = x2 - x1
    if u == 1: 
        return x1 % p
    else:
        return x2 % p
    

if __name__ == "__main__":
    p = int(input("Nhap p: "))
    n = int(input("Nhap so phan tu cua mang A: "))
    arr = []
    for i in range(0, n):
        x = int(input(f"A[{i}] = "))
        arr.append(x)
    res = []
    for i in range(0, n):
        res.append(BinaryInversionInFp(p, arr[i]))
    print(f"Mang A vua nhap la: {arr}")
    print(f"Mang B gom cac phan tu nghich dao cua cac phan tu tuong ung trong mang A la:\n{res}")
        