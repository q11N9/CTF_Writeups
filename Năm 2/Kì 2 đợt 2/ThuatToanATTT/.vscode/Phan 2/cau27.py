
def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
def eratothenes(n):
    sieves = [True] * n
    sieves[0] = sieves[1] = 0
    res = []
    for i in range(0, n):
        if sieves[i]:
            res.append(i)
            j = 2
            while i * j < n:
                sieves[i * j] = False
                j += 1
    return res
    
def coPrime(limits):        #Tim cac cap so nguyen to cung nhau
    coprimes = []
    for i in range(1, limits + 1):
        for j in range(i + 1, limits + 1):
            if gcd(i, j) == 1:
                coprimes.append((i, j))
    return coprimes

def generatePairs(prime, arr):
    for i in arr:
        print(f"a = {i[0] * prime}, b = {i[1] * prime}, gcd(a, b) = {prime}")
        

if __name__ == "__main__":
    primes = eratothenes(1000)
    coPrimes = coPrime(1000)
    for i in primes:
        generatePairs(i, coPrimes)