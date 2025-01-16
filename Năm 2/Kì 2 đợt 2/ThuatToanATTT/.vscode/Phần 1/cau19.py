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
def SNTbac2(a, b, c, m, l):
    res = []
    for i in range(m, l + 1):
        if isPrime(a*(i**2) + b*i + c) == 1 and i > 0:
            res.append(i)
    return res
if __name__ == "__main__":
    a = int(input("Nhap A: "))
    b = int(input("Nhap B: "))
    c = int(input("Nhap C: "))
    m = int(input("Nhap m: "))
    l = int(input("Nhap l: "))
    while l <= m:
        l = int(input("Vi pham dieu kien m < l, vui long nhap lai: "))
    res = SNTbac2(a, b, c, m, l)
    if len(res) == 0:
        print(f"Khong co so nguyen duong nao thoa man Ax^2 + Bx + C voi x nam trong khoang [{m}, {l}]")
    else:
        print(f"Cac so nguyen duong x thoa man {a}x^2 +{b}x + {c} voi x nam trong khoang [{m}, {l}] la {res}")