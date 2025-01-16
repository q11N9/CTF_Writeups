
def floyd(tortoise, hare, n):
    while(1):  
        tortoise = tortoise**2 + 1
        hare = hare**2 + 1
        hare = hare**2 + 1
        if tortoise % n == hare % n:
            break
    return gcd(tortoise - hare, n)
def pollardsRho(n):
    a = b = 2
    d = -1
    while d <= 1 or d >= n: 
        a = (a**2 + 1) % n
        b = (b**2 + 1) % n
        b = (b**2 + 1) % n
        d = gcd (a - b, n)
        if d > 1 and d < n: 
            return d
        elif d == n: 
            return -1
def gcd(a, b): 
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
if __name__ == "__main__":
    n = int(input("Nhap n: "))
    d = pollardsRho(n)
    if d == -1:
        print("n la so nguyen to")
    else: 
        print(f"Thua so khong tam thuong cua n la : {pollardsRho(n)}")