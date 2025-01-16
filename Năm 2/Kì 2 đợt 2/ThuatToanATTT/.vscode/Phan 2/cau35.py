import random
def squareAndMultiply(a, b, n):
    res = 1
    a = a % n
    while b > 0:
        if n % 2:
            res = (res*a) % n
            b = b - 1
        else:
            a = (a**2)* n
            n = n // 2
    return res % n
def find_r_and_s(n):
    n = n - 1
    count = 0
    while n != 1: 
        n = n // 2
        count += 1
        if n % 2 == 1: 
            return [count, n]
        
def millerRabinAlgorithm(n, t):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    rs = find_r_and_s(n)
    s = rs[0]
    r = rs[1]
    for i in range (1,t + 1):
        a = random.randint(2, n - 2)
        y = squareAndMultiply(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = squareAndMultiply(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1: 
                return False
    return True

if __name__ == "__main__":
    n = int(input("Nhap so nguyen n: "))
    t = -1 
    while t < 1:
        t = int(input("Nhap tham so an toan t >= 1: "))
    # for i in range(2, n):
    #     if millerRabinAlgorithm(i, t):
    #         print(i, end = " ")
    if millerRabinAlgorithm(n, t):
        print(f"{n} la so nguyen to")
        print(f"Xac suat de {n} la so nguyen to la {1 - (1/4)**t}")
    else:
        print(f"{n} khong la so nguyen to")
    