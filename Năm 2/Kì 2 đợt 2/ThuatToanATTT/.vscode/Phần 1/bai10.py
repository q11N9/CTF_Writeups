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

def soUocSo(N):
    soUoc = 1
    for i in range(1, int(N/2) + 1):
        if N % i == 0:
            soUoc += 1
    return soUoc

if __name__ == "__main__":
    n = int(input("Nhap n: "))
    print(f"So uoc cua n la {soUocSo(n)}, so uoc nguyen to cua n la {soUocNguyenTo(n)}")