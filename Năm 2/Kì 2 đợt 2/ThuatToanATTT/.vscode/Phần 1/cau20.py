import math
def findPrime(a, b):
    res = []
    isPrime = [1] * (b + 1)
    isPrime[0] = isPrime[1] = 0
    for i in range (2, int(math.sqrt(b) +  1)):
        if isPrime[i] == 1:
            j = 2
            while i*j <= b:
                isPrime[i*j] = 0
                j += 1
    for i in range(max(a, 2), b + 1):
        if isPrime[i] == 1:
            res.append(i)
        
    return res

if __name__ == "__main__":
    m = int(input("Nhap M: "))
    while m < 1: 
        m = int(input("m > 0, vui long nhap lai: "))
    n = int(input("Nhap N: "))
    while n <= m + 1 or n >= 1000:
        n = int(input("n < 100 va n > m + 1, vui long nhap lai: "))
    d = int(input("Nhap D: "))
    while d >= 1000 or d <= 0: 
        m = int(input("0 < d < 1000, vui long nhap lai: "))
    if d > n: 
        print("Khong co cap so nao thoa man")
    else: 
        upper = n//d
        bottom = m//d
        prime = findPrime(bottom, upper)
        if len(prime) < 2:
            print("Khong co cap so nao thoa man")
        else:
            res = []
            for i in prime:
                res.append(i*d)
            print(f"Cac cap so co uoc chung lon nhat la {d} trong khoang ({m}, {n}) la: ")
            for i in range (0, len(res) - 1):
                for j in range(i + 1, len(res)):
                    print(f"[{res[i], res[j]}]", end=", ")
            