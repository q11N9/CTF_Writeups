import math
def prime(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = 0
    res = []
    for i in range (2, n +  1):
        if sieve[i] == True:
            res.append(i)
            j = 2
            while i * j <= n:
                sieve[i * j] = False
                j += 1
    return res
def strongNumber(N):
    if N < 4: 
        return []
    litmit = math.ceil(math.sqrt(N))
    primes = prime(litmit)
    strongNumbers = [False] * N
    for i in primes:
        j = 1
        while i**2 * j < N:
            strongNumbers[i**2 * j] = True
            j += 1
    res = []
    for i in range(0, len(strongNumbers)):
        if strongNumbers[i] == True:
            res.append(i)
    return res
    

if __name__ == "__main__": 
    N = int(input("Nhap N < 10000"))
    while N <= 0 or N >= 10000:
        N = int(input("Vui long nhap N nguyen duong va nho hon 10000: "))
    res = strongNumber(N)
    print(f"Cac so manh me nho hon N la: {res}")