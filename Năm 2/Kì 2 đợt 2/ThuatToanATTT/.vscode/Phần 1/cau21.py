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

def countPrime(n):
    if n < 3: 
        return 0
    count = 0
    for i in range(2, n):
        if isPrime(i) == 1:
            count += 1
    return count

    

if __name__ == "__main__":
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    while b <= a:
        b = int(input("b phai lon hon a, vui long nhap lai: "))
    if b < 4: 
        print("Khong co so sieu nguyen to nao nam giua [a, b]")
    else:
        res = []
        index = a + 1
        prevPrime = countPrime(a)
        if isPrime(prevPrime) == 1:
            res.append(a)
        while index <= b:
            for i in range(a, index):
                if isPrime(i):
                    prevPrime += 1
            if isPrime(prevPrime) == 1: 
                res.append(index) 
            index += 1
        if len(res) == 0:
            print("Khong co so sieu nguyen to nao thoa man")
        else:
            print(f"So cac so sieu nguyen to nam trong khoang [a,b] la: {len(res)} va cac so do la: {res}")