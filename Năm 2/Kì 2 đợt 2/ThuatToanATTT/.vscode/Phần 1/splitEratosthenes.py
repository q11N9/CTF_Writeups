import math

def eratosthenes(n):
    prime = [1] * n
    prime[0] = prime[1] = 0
    res = []
    if n < 2: 
        return res
    for i in range(2, n):
        if prime[i] == 1:
            res.append(i)
            j = 2
            while i * j < n:
                prime[i * j] = 0
                j += 1
    return res
def splitEratothenes(n):
    prime = [1] * (n + 1)
    prime[0]  = prime[1] = 0
    step = math.ceil(math.sqrt(n))
    i = 0
    j = step
    res = eratosthenes(j)   #Tim cac so nguyen to nho hon sqrt(n)
    i += step               #Di chuyen den mang tiep theo
    j += step
    while j <= n: 
        dummy = math.ceil(math.sqrt(j))             #Tim phan tu lon nhat cua doan dang xet
        for k in res:                               #Xet cac phan tu o trong mang luu tru SNT
            if k <= dummy:
                multiple = math.ceil(i/k)          #Boi cua k 
                while k * multiple < j:
                    prime[multiple * k] = 0
                    multiple += 1
        if j > n:
            j = n + 1
        for r in range(max(i, 2), j):
            if prime[r] == 1:
                res.append(r)
        i += step
        j += step
    return res
        
if __name__ == "__main__": 
    n = int(input("Nhap n: "))
    while n < 0: 
        n = int(input("Vui long nhap n lon hon 0"))
    print(f"Cac so nguyen to nho hon hoac bang n la: {splitEratothenes(n)}")