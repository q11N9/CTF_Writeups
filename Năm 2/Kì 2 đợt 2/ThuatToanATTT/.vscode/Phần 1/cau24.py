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
def checkSumSquare(n):
    limit = int(math.sqrt(n))
    for i in range(1, limit + 1):
        left = n - i**2
        sqrt_left = int(math.sqrt(left))
        if sqrt_left**2 == left:
            return 1
    return 0

if __name__ == "__main__":
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    res = []
    for i in range(a, b + 1):
        if checkSumSquare(i) == 1 and Prime(i) == 1:
            res.append(i)
    print(f"Tat ca cac so nguyen to trong khoang [a, b] va la so nguyen to la: {res}")