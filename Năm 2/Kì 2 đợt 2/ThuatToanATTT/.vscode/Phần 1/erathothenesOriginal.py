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

if __name__ == "__main__": 
    n = int(input("Nhap n: "))
    while n < 0: 
        n = int(input("Vui long nhap n lon hon 0"))
    print(f"Cac so nguyen to nho hon hoac bang n la: {eratosthenes(n)}")