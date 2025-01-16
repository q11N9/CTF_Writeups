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
if __name__ == "__main__":
    n = int(input("Nhap n:"))
    print(f"Cac so nguyen to co {n} chu so la: ")
    count = 0
    for i in range(10**(n-1), 10**n):
        if isPrime(i):
            count+=1
            print(f"{i:-11d}", end = "")
            if count == 5:
                count = 0
                print("")