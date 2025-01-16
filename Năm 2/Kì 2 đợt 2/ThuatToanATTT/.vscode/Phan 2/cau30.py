import math
def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def nhanBinhPhuong(a, b, n):
    res = 1
    a = a % n
    while b > 0:
        if n % 2:
            res = (res*a) % n
            b = b - 1
        else:
            a = (a**2)* n
            n = n // 2
    return res % n

def coPrime(n):     #Tim cac so nguyen to cung nhau voi n va nho hon n
    res = []
    for i in range(1, n): 
        if gcd(i, n) == 1:
            res.append(i)
    return res
    
def isComposite(n):
    if n < 4:
        return False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False
def CamichaelNumber(n):
    
    if isComposite(n):
        coPrimes = coPrime(n)
        for i in coPrimes:
            if nhanBinhPhuong(i, n - 1, n) != 1: 
                return False
        return True
    else:
        return False

if __name__ == "__main__": 
    N = int(input("Nhap N: "))
    if N < 4:
        print("Khong co so Camichael nao thoa man")
    else:
        res = []
        for i in range(1, N):
            if CamichaelNumber(i):
                res.append(i)
        print(f"Tong cac so Camilchael nho hon n la: {sum(i for i in res)}")