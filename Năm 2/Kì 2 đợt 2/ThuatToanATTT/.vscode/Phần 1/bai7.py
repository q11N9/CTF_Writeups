import math

def isPrime(n):
    if n < 2 : 
        return 0
    if n == 2: 
        return 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 1
    return 1

def reverseNumber(n):
    reversed_n = 0
    while n != 0:
        reversed_n = reversed_n * 10 + n % 10
        n = int(n / 10)
    return reversed_n
def emirpNumber(n):
    sieve = [1] * n
    sieve[0] = sieve[1] = 0
    emirp = []
    for i in range(2, n):
        if sieve[i] == 1:
            if isPrime(reverseNumber(i)) == 1:
                emirp.append(i)
            j = 2
            while i * j < n:
                sieve[i*j] = 0
                j += 1
    return emirp

if __name__ == "__main__":
    n = int(input("Nhap N: "))
    emirp = emirpNumber(n)
    if len(emirp) == 0:
        print("Khong co so emirp nao nho hon N")
    else: 
        print(f"Cac so emirp nho hon N la: {emirp}")   