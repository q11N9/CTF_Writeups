import random
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
def generateList(lower, upper, size):
    return [random.randint(lower, upper) for _ in range(size)]
def find_primes(arr):
    return [num for num in arr if isPrime(num)]

if __name__ == "__main__":
    n = int(input("Nhap kich thuoc mang: "))
    while n < 0:
        n = int(input("Kich thuoc mang phai lon hon 0, vui long nhap lai: "))
    lower = int(input("Nhap gioi han duoi: "))
    upper = int(input("Nhap gioi han tren: "))
    if upper <= lower:
        upper = int(input("Gioi han tren phai lon hon gioi han duoi, vui long nhap lai: "))
    res = generateList(lower, upper, n)
    print(f"Mang sinh la: {res}")
    res = find_primes(res)
    res.sort()
    if len(res) == 0:
        print("Khong co so nguyen to nao co trong mang vua sinh")
    else:
        print(f"Cac so nguyen to co trong mang vua sinh la: {res}")