import math
def isPrime(p):
    if p < 2:
        return 0
    if p == 2:
        return 1
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0: 
            return 0
    return 1

def haiSNT(n):
    if n < 3:
        print("Khong co hai so nguyen to nao ma tong va hieu cua chung deu la so nguyen to")
    else:
        sieve = [1] * (n + 1)
        sieve[0] = sieve[1] = 0
        snt = []
        for i in range (2, n + 1):
            if sieve[i] == 1:
                snt.append(i)
                j = 2
                while i * j <= n:
                    sieve[i * j] = 0
                    j += 1
        i = 1
        length = len(snt)
        res = []
        while i < length:
            if isPrime(snt[0] + snt[i]) and isPrime(snt[i] - snt[0]):
                res.append([snt[0], snt[i]])
            i += 1
        if len(res) == 0:
            print("Khong co cap so nguyen to nao thoa man")
        else:
            print(f"Nhung cap so nguyen to nho hon hoac bang n ma tong va hieu cua chung la 1 so nguyen to la: {res}")    
        
if __name__ == "__main__":
    n = int(input("Nhap n: ")) 
    haiSNT(n)