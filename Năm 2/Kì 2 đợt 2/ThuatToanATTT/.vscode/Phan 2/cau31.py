import math
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

def eratosthenes(n):
    prime = [1] * (n + 1)
    prime[0] = prime[1] = 0
    res = []
    if n < 2: 
        return res
    for i in range(2, n + 1):
        if prime[i] == 1:
            res.append(i)
            j = 2
            while i * j <= n:
                prime[i * j] = 0
                j += 1
    return res
    
def findNearestPrime(n):
    primes = eratosthenes(n)        #Tim tat ca ca so nguyen to nho hon n
    nearPrime = primes[len(primes) - 1]     #Tim so nguyen to nho hon hoac bang n
    if nearPrime == n:
        return n
    space = n - nearPrime
    sieve2 = [True] * (n + space + 1)           #Tim tat ca so nguyen to trong khoang (n, n + space]
    for i in primes:            
        if i > math.ceil(math.sqrt(n + space)) + 1:
            break
        else: 
            j = n // i
            while i * j <= n + space:
                sieve2[i * j] = False
                j += 1
    
    for i in range(n + 1, n + space + 1):
        if sieve2[i] == True:
            if i - n >= space:
                return nearPrime
            if i - n < space:
                return i
    return nearPrime
    
if __name__ == "__main__":
    msv = int(input("Nhap ma sinh vien(6 chu so cuoi): "))
    nearestPrime = findNearestPrime(msv)
    print(f"So nguyen to gan nhat voi ma sinh vien la: {nearestPrime} ")
    sbd = int(input("Nhap sbd: "))
    print(f"{sbd}^{nearestPrime} = {nhanBinhPhuong(sbd,nearestPrime,123456)}")
    