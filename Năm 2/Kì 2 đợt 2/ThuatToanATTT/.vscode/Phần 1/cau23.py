import math
def Prime(n):
    if n < 2:
        return 0
    if n == 2: 
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def sumPrimeBetween(a, b):
    sum = 0
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
            sum += i
    return sum

if __name__ == "__main__":
    a = int(input("Nhap A: "))
    b = int(input("Nhap B: "))
    tongSNT = sumPrimeBetween(a,b)
    print(f"Tong cac so nguyen to nam giua a va b la: {tongSNT}")
    if Prime(tongSNT):
        print("==> Yes")
    else:
        print("==> No")

    