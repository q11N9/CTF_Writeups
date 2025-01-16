import random
import math
#c la ban ma, e la public key, d la private key
def nhanBinhPhuong(a, k, n):
    b = 1
    if k == 0:
        return b
    bin_k = bin(k)[2:]
    l = len(bin_k)
    if bin_k[l - 1] == '1':
        b = a
    for i in range(l - 2, -1, -1):
        a = (a**2) % n 
        if bin_k[i] == '1':
            b = (a*b) % n
    return b

        
def millerRabinAlgorithm(n, t):
    def find_r_and_s(n):
        n = n - 1
        count = 0
        while n != 1: 
            n = n // 2
            count += 1
            if n % 2 == 1: 
                return [count, n]
    rs = find_r_and_s(n)
    s = rs[0]
    r = rs[1]
    for i in range (1,t + 1):
        a = random.randint(2, n - 2)
        y = nhanBinhPhuong(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = (y**2) % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1: 
                return False
    return True

def eratosthenes(a,b):
    res = []
    isPrime = [1] * (b + 1)
    isPrime[0] = isPrime[1] = 0
    for i in range (2, int(math.sqrt(b) +  1)):
        if isPrime[i] == 1:
            j = 2
            while i*j <= b:
                isPrime[i*j] = 0
                j += 1
    for i in range (2, b + 1):
        if isPrime[i] == 1 and i >= a:
            res.append(i)
    return res

def generate_Prime():
    sieves = eratosthenes(100, 500)
    return random.choice(sieves)
def bieuDienMang(a, w, t):
    arr = []
    while(t > 0):
        x = 2**(w*(t - 1))
        arr.append(int(a/x))
        a -= int(a/x)*x
        t -= 1
    return arr

def convertInterger(arr,  w, t):
    sum = 0
    index = 0
    j = 0
    while j <= t - 1:
        x = 2**(w*j)
        sum += arr[index]*x
        j += 1
        index +=1
    return sum


def nhan_operand(a, b, t, w):
    def tinh8bit(n):
        bit8 = []
        sum_8bitdau = 0
        sum_8bitcuoi = 0
        for i in range (0, 8):
            x = int(n/2**(15-i))
            sum_8bitdau += x*2**(7-i)
            n -= x*2**(15-i)
        sum_8bitcuoi = n
        bit8.append(sum_8bitdau)
        bit8.append(sum_8bitcuoi)
        return bit8
    arr_a = bieuDienMang(a, w, t)
    arr_b = bieuDienMang(b, w, t)
    
    c = []
    for i in range (0, 2*t):
        c.append(0)
    for i in range (0, t):
        u = 0
        for j in range (0, t):
            uv = c[i+j] + arr_a[t - i - 1]*arr_b[t - j - 1] + u
            bit8 = tinh8bit(uv)
            u = bit8[0]
            v = bit8[1]
            c[i+j] = v
        c[i+t] = u
    return convertInterger(c, w, t)



def gcd(a, b):
    while b > 0:
        r = a% b
        a = b
        b = r
    return a

def findCoprime(n):
    for i in range(3, n):
        if gcd(i, n) == 1:
            return i

def findInversion(a, b):
    if b == 0:
        d, x, y =a, 1, 0
        return [d, x, y]
    x2, x1, y2, y1 = 1, 0, 0, 1
    while b > 0:
        q = a//b
        r = a - q*b
        x = x2 - q*x1
        y = y2 - q*y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    d, x, y = a, x2, y2
    return [d, x, y]

def code():
    t = 4
    w = 8
    p = generate_Prime()
    q = generate_Prime()
    while p == q:
        q = generate_Prime()
    n = nhan_operand(p, q, w, t)        #Tim n
    
    phi_n = nhan_operand(p - 1, q- 1,w, t)        #Tim phi_n
    e = findCoprime(phi_n)
    return [e, n, p, q]

def decode(c, e, n):           #Tim d 
    limit = math.ceil(math.sqrt(n))
    p = q = 0
    primes = eratosthenes(0, limit)
    for i in primes:
        j = n // i
        if i * j == n and millerRabinAlgorithm(j, 100) and i > 2:
            p = i
            q = j
    phi_n = nhan_operand(p - 1, q - 1, 4, 8) 
    d = findInversion(e, phi_n)[1]
    if d < 0:
        d += phi_n
    return nhanBinhPhuong(c, d, n)
            
if __name__ == "__main__":
    sbd = int(input("Nhap so bao danh: "))
    m = sbd + 123
    e_n = code()
    e = e_n[0]
    n = e_n[1]

    c = nhanBinhPhuong(m, e, n)
    print(f"Voi public key e = {e}, n = {n}, ban ma c cua thong diep m la: c = {c}")
    print(f"Thong diep duoc giai ma la: {decode(c,e,n)}")
    
    