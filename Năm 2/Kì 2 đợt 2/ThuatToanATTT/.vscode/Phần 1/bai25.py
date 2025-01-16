import math
def findCombination(arr, target, amount):
    def backtrack(start, target, temp):
        if target == 0 and len(temp) == amount:  # neu co thi cho vao mang combinations roi ket thuc 
            combinations.append(temp[:])
            return
        if target < 0 or len(temp) >= amount:       #Xet cac truong hop khac
            return
        for i in range(start, len(arr)):  
            temp.append(arr[i])
            backtrack(i + 1, target - arr[i], temp)         #Tim xem target - arr[i] co the bieu dien bang cac so con lai ke tu i + 1 khong 
            temp.pop()              #Reset mang temp(qua moi vong lap, pop tung phan tu)
            
    combinations = []
    backtrack(0, target, [])            
    return combinations

def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True 
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sieveOfEratothenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = 0
    res = []
    for i in range(2, n + 1):
        if sieve[i]:
            res.append(i)
            j = 2
            while i * j <= n:
                sieve[i * j] == False
                j += 1
    return res
def checkSumN(n, m):
    primes = sieveOfEratothenes(n)
    isSum = [[False] * (n + 1) for i in range(m + 1)]
    isSum[0][0] = True
    for prime in primes:
        for i in range(m, 0, -1):
            for j in range(n, prime - 1, -1):
                if isSum[i - 1][j - prime]:         #Check if n - prime can be express to sum m - 1 prime numbers or not
                    isSum[i][j] = True  #Neu co thi n cung bieu dien duoc thanh tong m so nguyen to
    for i in range(0, n + 1):
        if isPrime(i) == False:
            isSum[1][i] = False
    if isSum[m][n] == False:
        print(f"{n} khong the phan tich ra thanh tong cua {m} so nguyen to")
    else:
        print(f"{n} co the duoc phan tich ra thanh tong cua {m} so nguyen to.")
        combinations = findCombination(primes, n, m)
        res = []
        for i in combinations:
            all_primes = True
            for j in i: 
                if isPrime(j) == False:
                    all_primes = False
                    break
            if all_primes == True:
                res.append(i)
        print(f"Cac bo so co the bieu dien la: {res}")
    
if __name__ == "__main__":
    N = int(input("Nhap N: "))
    M = int(input("Nhap M: "))
    checkSumN(N, M)