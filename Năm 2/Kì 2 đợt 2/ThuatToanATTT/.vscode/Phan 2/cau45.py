import random
def nhanBinhPhuong(a, k, n):
    b = 1
    if k == 0:
        return b
    bin_k = bin(k)[2:]
    l = len(bin_k)
    if bin_k[l - 1] == '1':
        b = a
    for i in range(l - 2, -1, -1):
        a = (a**2) % n 
        if bin_k[i] == '1':
            b = (a*b) % n
    return b
def find_r_and_s(n):
    n = n - 1
    count = 0
    while n != 1: 
        n = n // 2
        count += 1
        if n % 2 == 1: 
            return [count, n]
        
def millerRabinAlgorithm(n, t):
    rs = find_r_and_s(n)
    s = rs[0]
    r = rs[1]
    for i in range (1,t + 1):
        a = random.randint(2, n - 2)
        y = nhanBinhPhuong(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = nhanBinhPhuong(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1: 
                return False
    return True

def eratosthenes(n):
    prime = [1] * (n + 1)
    prime[0] = prime[1] = 0
    res = []
    if n < 2: 
        return res
    for i in range(2, n + 1):
        if prime[i] == 1:
            res.append(i)
            j = 2
            while i * j <= n:
                prime[i * j] = 0
                j += 1
    return res
def checkPrime(p, t):
    if p == 2 or p ==3:
        return True
    if p < 2 :
        return False
    res = eratosthenes(p)
    count = 0
    for i in res:               #Chia thu cho vai so nguyen to dau
        if p % i == 0 and i < p:
            count = 1
            break
    if count == 0:
        if millerRabinAlgorithm(p, t):
            return True
    else: 
        return False
def generate_Prime(t):
    while True:
        n = random.randint(0,1000)
        if checkPrime(n, t):
            return n
        

if __name__ == "__main__":
    N = int(input("Nhap N: "))
    arr = []
    for i in range(0, N):
        x = generate_Prime(3)
        arr.append(x)
    print(f"Mang vua duoc sinh ra la: {arr}")
    prev = arr[0]
    min = arr[0]
    for i in arr:
        if min > i:
            prev = min
            min = i
    print(f"Khoang cach nho nhat giua 2 phan tu bat ki trong mang la: {abs(prev - min)}")