import random
def squareAndMultiply(a, k, n):
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
def fermatAlgorithm(n, t):
    r = -1
    for i in range(0, t):
        a = random.randint(2, n - 2)
        r = squareAndMultiply(a, n - 1, n)
        if r != 1:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Nhap so nguyen n le, n >= 3: "))
    while n % 2 == 0 or n < 3:
        n = int(input("Nhap so nguyen n le, n >= 3: "))
    t = -1 
    while t < 1:
        t = int(input("Nhap tham so an toan t >= 1: "))
        
    if fermatAlgorithm(n, t):
        print(f"{n} la so nguyen to")
    else:
        print(f"{n} khong la so nguyen to")
    
    
#Thuat toan se sai voi cac so Camichael, vi du [561, 1105, 1729, 2465, 2821, 6601, 8911]