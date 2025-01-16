import random
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
def checkPrime(p):
    if p < 2: 
        return False
    if p == 2 or p == 3:
        return True
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
    if millerRabinAlgorithm(p, 5):
        return True
    return False

if __name__ == "__main__":
    a = int(input("Nhap a: "))
    k = int(input("Nhap k: "))
    n = int(input("Nhap n: "))
    res = nhanBinhPhuong(a, k, n)
    print(f"{a}^{k} mod {n} = {res} ", end = "")
    if checkPrime(res):
        print("la mot so nguyen to")
    else:
        print("khong la 1 so nguyen to")