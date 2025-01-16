import math
def demSNT(n):
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
    return len(count)
if __name__ == "__main__":
    n = int(input("Nhap n: "))
    print(f"So so nguyen to nho hon hoac bang N la: {demSNT(n)}")
    