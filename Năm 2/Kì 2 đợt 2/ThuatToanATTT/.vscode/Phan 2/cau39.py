import random
import math
def checkPrime(p,t):
    if p < 2: 
        return False
    if p == 2 or p == 3:
        return True
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
            r = n - 1
            s = 0
            while r % 2 == 0: 
                r = r // 2
                s += 1
            return s, r
        s, r = find_r_and_s(n)
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
    if millerRabinAlgorithm(p, t):
        return True
    return False
def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
def gcd_prime_pairs(arr, t):
    res = []
    l = len(arr)
    for i in range(0, l - 1):
        for j in range(i + 1, l):
            if checkPrime(gcd(arr[i], arr[j]), t):
                res.append((arr[i], arr[j]))
    return res
if __name__ == "__main__":
    n = int(input("Nhap so phan tu cua mang: "))
    # arr = [
    # 10234, 15678, 23456, 34567, 45678, 56789, 67890, 78901, 89012, 90123,
    # 11223, 22334, 33445, 44556, 55667, 66778, 77889, 88990, 99001, 10011,
    # 11112, 22223, 33334, 44445, 55556, 66667, 77778, 88889, 99990, 10001
    # ]
    arr = []
    for i in range(0, n):
        x = int(input(f"a[{i}] = "))
        arr.append(x)
    t = int(input("Nhap t: "))
    gcd_primes = gcd_prime_pairs(arr, t)
    if len(gcd_primes) == 0:
        print("Khong co cap so nao thoa man")
    else:
        print(f"Cac cap so co uoc chung lon nhat la 1 so nguyen to la: {gcd_primes}")