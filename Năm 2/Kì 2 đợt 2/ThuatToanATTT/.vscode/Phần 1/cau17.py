import math
def isPrime(n):
    if n < 2: 
        return 0
    if n == 2:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1
def SNTbac2(a, b, c):
    if isPrime(a + b + c) == 1:
        return 1
    x = 1
    while isPrime(a*(x**2) + b*x + c) == 0:
        x += 1
    return x
if __name__ == "__main__":
    a = int(input("Nhap A: "))
    b = int(input("Nhap B: "))
    c = int(input("Nhap C: "))
    print(f"So nguyen duong x nho nhat de {a}x^2 + {b}x + {c} la 1 so nguyen to la: {SNTbac2(a,b,c)}")