import math
def isPrime(p):
    if p < 2:
        return 0
    if p == 2:
        return 1
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0: 
            return 0
    return 1

def soUocNguyenTo(N):
    if isPrime(N) == 1:
        return N
    soUoc = 0
    for i in range (2, int(N/2) + 1):
        if N % i == 0 and isPrime(i) == 1:
            soUoc += 1
    return soUoc

def tongUocNguyenTo(N):
    if isPrime(N) == 1:
        return N
    sum = 0
    for i in range (2, int(N/2) + 1):
        if N % i == 0 and isPrime(i) == 1:
            sum += i
    return sum
def tongUocSo(N):
    sum = N
    for i in range(1, int(N/2) + 1):
        if N % i == 0:
            sum += i
    return sum
def soUocSo(N):
    soUoc = 1
    for i in range(1, int(N/2) + 1):
        if N % i == 0:
            soUoc += 1
    return soUoc
if __name__ == "__main__":
    N = int(input("Nhap N: "))
    while N < 1:
        N = int(input("N phai la 1 so nguyen duong, vui long nhap lai: "))
    if N == 1: 
        print("Vay N + p + s - q - k =  1 + 1 + 1 - 0 - 0 = 3")
    else: 
        k = soUocNguyenTo(N)
        q = tongUocNguyenTo(N)
        p = tongUocSo(N)
        s = soUocSo(N)
        print(f"Vay N + p + s - q - k = {N} + {p} + {s} - {q} - {k} = {N + p + s - q - k}")