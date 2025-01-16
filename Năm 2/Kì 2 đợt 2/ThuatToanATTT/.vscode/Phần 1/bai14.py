import math
def cubed(n):
    a = int(n**(1/3))
    if a**3 == n:
        return 1
    else:
        return 0
    
def reverseNumber(n):
    reversed_n = 0
    while n != 0:
        reversed_n = reversed_n * 10 + n % 10
        n = int(n / 10)
    return reversed_n

def reversedPrime():
    sieve = [1] * 1000
    sieve[0] = sieve[1] = 0
    count = []
    for i in range (2, 1000):
        if sieve[i] == 1:
            if i >= 100: 
                count.append(i)
            j = 2
            while i * j <= 999:
                sieve[i * j] = 0
                j += 1 
    res = []
    for i in count:
        if cubed(reverseNumber(i)) == 1:
            res.append(i)
    print(f"Cac so nguyen to co ba chu so ma so dao nguoc cua no la lap phuong cua 1 so la: {res}")

if __name__ == "__main__":
    reversedPrime()