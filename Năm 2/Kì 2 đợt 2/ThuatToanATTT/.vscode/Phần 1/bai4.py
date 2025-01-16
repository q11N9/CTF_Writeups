import math
def countPrime(a, b):
    count = 0
    isPrime = [1] * (b + 1)
    isPrime[0] = isPrime[1] = 0
    for i in range (2, int(math.sqrt(b) +  1)):
        if isPrime[i] == 1:
            j = 2
            while i*j <= b:
                isPrime[i*j] = 0
                j += 1
    for i in range (2, b + 1):
        if isPrime[i] == 1 and i >= a:
            count += 1
    return count

if __name__ == "__main__":
    a = int(input("Nhap A: "))
    b = int(input("Nhap B: "))
    print(f"So so nguyen to trong khoang [A, B] la: {countPrime(a, b)}")
    