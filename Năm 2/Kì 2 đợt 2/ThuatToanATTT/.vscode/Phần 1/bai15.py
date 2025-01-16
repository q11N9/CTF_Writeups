

def twinPrime(n):
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    count = []
    for i in range (2, n + 1):
        if sieve[i] == 1:
            count.append(i)
            j = 2
            while i * j <= n:
                sieve[i * j] = 0
                j += 1 
    res = []
    length = len(count)
    j = 0
    while j < length - 1:
        if count[j + 1] - count[j] == 2:
            res.append([count[j], count[j+1]])
        j += 1
    return res

if __name__ == "__main__":
    n = int(input("Nhap n: "))
    if n < 5:
        print("Khong co cap so nguyen to sinh doi nao")
    else:
        print(f"Cac cap so nguyen to sinh doi nho hon hoac bang n la: {twinPrime(n)}")