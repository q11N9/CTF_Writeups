import math
def tPrime(n):
    if n < 3: 
        return 0
    count = 0
    for i in range (2, int(n/2) + 1):
        if n % i == 0:
            count += 1
        if count > 1: 
            return 0
    return count == 1

if __name__ == "__main__":
    n = int(input("Nhap n: "))
    tPrimeNumber = []
    if n < 3: 
        print("Khong co so nao thoa man")
    else: 
        for i in range(4, n+1):
            if tPrime(i) == 1:
                tPrimeNumber.append(i)
    print(f"Cac so T-Prime nho hon hoac bang N la: {tPrimeNumber}")