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

def tinhFn(N):
    if isPrime(N) == 1:
        return N 
    else: 
        return 0

if __name__ == "__main__":
    L = int(input("Nhap L: "))
    R = int(input("Nhap R: "))
    if (L <= 0 and R <= 0) or (L >= 10000 and R >= 10000) or (R <= L):
        print("L va R phai nam trong khoang (0, 10000) va R > L. Vui long nhap lai")
        L = int(input("Nhap L: "))
        R = int(input("Nhap R: "))
    i = L
    j = i + 1
    while i < R:
        F_i = tinhFn(i)
        F_j = tinhFn(j)
        print(f"Voi i, j = [{i}, {j}]Tich F({i})*F({j}) = {F_i * F_j}")
        j += 1
        if j == R + 1:
            i += 1
            j = i + 1
        