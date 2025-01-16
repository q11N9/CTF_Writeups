import math
# Vi tong cua 4 so la 1 so nguyen to ma 4 so nguyen to deu la so le nen tong cua chung la so chan, nen chi co 1 bo (2,3,5,7) thoa man
def isPrime(p):
    if p < 2:
        return 0
    if p == 2:
        return 1
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0: 
            return 0
    return 1

def tongBonSNT(n):
    if n < 7:
        print("Khong co 4 so nguyen to nao thoa man")
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
        i = 0
        length = len(snt)
        res = []
        while(i < length - 3):
            x = 0
            for j in range(0, 4):
                x += snt[i + j]
            if isPrime(x) == 1 and x <= n:
                res.append([snt[i], snt[i + 1], snt[i + 2], snt[i + 3]])
            i += 1
        if len(res) == 0:
            print("Khong co 4 so nguyen to lien tiep nao thoa man")
        else:
            print(f"Nhung bo 4 so nguyen to lien tiep ma tong cua chung la 1 so nguyen to nho hon hoac bang n la: {res}")     
if __name__ == "__main__":
    n = int(input("Nhap n: "))
    tongBonSNT(n)