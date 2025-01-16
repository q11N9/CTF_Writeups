import random
import math
def checkPrime(p):
    def nhanBinhPhuong(a, k, n):
        b = 1
        if k == 0:
            return b
        bin_k = bin(k)[2:]
        l = len(bin_k)
        if bin_k[l - 1] == '1':
            b = a
        for i in range(l - 2, -1, -1):
            a = (a**2) % n 
            if bin_k[i] == '1':
                b = (a*b) % n
        return b

        
    def millerRabinAlgorithm(n, t):
        def find_r_and_s(n):
            n = n - 1
            count = 0
            while n != 1: 
                n = n // 2
                count += 1
                if n % 2 == 1: 
                    return [count, n]
        rs = find_r_and_s(n)
        s = rs[0]
        r = rs[1]
        for i in range (1,t + 1):
            a = random.randint(2, n - 2)
            y = nhanBinhPhuong(a, r, n)
            if y != 1 and y != n - 1:
                j = 1
                while j <= s - 1 and y != n - 1:
                    y = (y**2) % n
                    if y == 1:
                        return False
                    j += 1
                if y != n - 1: 
                    return False
        return True
    if millerRabinAlgorithm(p, 5):
        return True
    return False
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
    p = int(input("Nhap so nguyen to p: "))
    while(checkPrime(p) == 0):
        p = int(input("p phai la mot so nguyen to, vui long nhap lai: "))
    a = int(input("Nhap a nam trong khoang [1, p-1]: "))
    while(a < 1 or a >= p):
        a = int(input("So vua nhap khong hop le, vui long thu lai: "))
    print(f"Nghich dao cua a module p (a^-1 mod p) la: {BinaryInversionInFp(p, a)}")