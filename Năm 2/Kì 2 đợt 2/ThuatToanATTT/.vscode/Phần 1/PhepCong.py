import math
def bieuDienMang(a, w, t):
    arr = []
    while(t > 0):
        x = 2**(w*(t - 1))
        arr.append(int(a/x))
        a -= int(a/x)*x
        t -= 1
    return arr

def checkPrime(p):
    if p < 2: 
        return 0
    if p == 2: 
        return 1
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return 0
    return 1

def congTruongHH(a, b, t, w):
    r = 2**w
    epsilon = 0
    c = []
    c.insert(0,(a[3] + b[3])% r)
    if a[3] + b[3] >= r:
        epsilon = 1
    for i in range(1, t):
        x = a[t - 1 - i] + b[t - 1 - i] + epsilon
        c.insert(0, x  % r)
        if x >= r:
            epsilon = 1
        else: 
            epsilon = 0
    return (epsilon, c)


def truTruongHH(a, b, t, w):
    r = 2**w
    epsilon = 0
    c = []
    c.insert(0,(a[3] - b[3])% r)
    if a[3] - b[3] >= r:
        epsilon = 1
    for i in range(1, t):
        x = a[t - 1 - i] - b[t - 1 - i]- epsilon
        c.insert(0, x  % r)
        if x >= r or x < 0:
            epsilon = 1
        else: 
            epsilon = 0
    return (epsilon, c)  

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

def nhan_operand(a, b, t, w):
    c = []
    for i in range (0, 2*t):
        c.append(0)
    for i in range (0, t):
        u = 0
        for j in range (0, t):
            uv = c[i+j] + a[t - i - 1]*b[t - j - 1] + u
            bit8 = tinh8bit(uv)
            u = bit8[0]
            v = bit8[1]
            c[i+j] = v
        c[i+t] = u
    return c


def luy_thua(p, b, k, z, u):
    c = b**(k-1)
    q = math.floor((z/ c) * (u/c))
    r = (z % c) - ((q*p)%c)
    if r < 0: 
        r = r + c
    while r >= p: 
        r = r - p
    return r

def euclide_mo_rong(a, b): 
    d = 1
    x = y = 0
    if b == 0:
        d = a
        x = 1
        y = 0
        return(d, x, y)
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while b > 0: 
        q = math.floor(a/b)
        r = a - q*b
        x = x2 - q*x1
        y = y2 - q*y1 
        a = b
        b = r
        x2 = x1 
        x1 = x
        y2 = y1
        y1 = y
    d = a
    x = x2 
    y = y2
    return (d, x, y)

def nghichDao(p, a):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = math.floor(v/u)
        r = v - q*u
        x = x2 - q*x1
        
        v = u
        u = r
        x2 = x1 
        x1 = x
    return x1 % p

def Binary_gcd(a, b):
    u = a
    v = b
    e = 1
    while u % 2 == 0 and v % 2 == 0:
        u = int(u/2)
        v = int(v/2)
        e = 2*e
    while u != 0 :
        while u % 2 == 0:
            u = int(u/2)
        while v % 2 == 0:
            v = int(v/2)
        if u >= v: 
            u = u - v
        else:
            v = v - u
    return e*v
def BinaryInversionInFp(p, a):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1 and v != 1 : 
        while u % 2 == 0:
            u = int(u/2)
            if x1 % 2 == 0: 
                x1 = int(x1 / 2)
            else:
                x1 = int((x1 + p) / 2)
        while v % 2 == 0: 
            v = v / 2
            if x2 % 2 == 0:
                x2 = int(x2/2)
            else: 
                x2 = int((x2 + p) / 2)
        if u >= v: 
            u = u - v
            x1 = x1 - x2
        else:
            v = v - u
            x2 = x2 - x1
    if u == 1: 
        return x1 % p
    else:
        return x2 % p
def partialMontInversionInFp(p, a, n): 
    u, v, x1, x2, k = a, p, 1, 0, 0
    while v > 0: 
        if v % 2 == 0: 
            v, x1 = int(v/2), 2*x1
        elif u % 2 == 0:
            u, x2 = int(u/2), 2*x2
        elif v >= u:
            v = int((v - u) / 2)
            x2 = x2 + x1
            x1 = 2*x1
        else:
            u = int((u- v) / 2)
            x1 = x2 + x1
            x2 = 2*x2
        k = k + 1
    if u != 1: 
        print("Not invertible")
    if x1 > p:
        x1 = x1 - p
    print(f"Ket qua la {[x1, k]} voi x = {x1} = a^-1 * 2^k mod p ")
    
    
if __name__ == "__main__": 
    w = 0
    p = 0
    a = 0
    b = 0
    arr_a = []
    arr_b = []
    choice = -1
    while(choice != 0):
        print("========================Menu=======================")
        print("0. Thoat")
        print("1. Cong")
        print("2. Tru")
        print("3. Nhan")
        print("4. Luy thua")
        print("5. Thuat toan Euclide mo rong tim GCD")
        print("6. Nghich dao tren truong F_p su dung thuat toan Euclide mo rong")
        print("7. Binay GCD algorithm")
        print("8. Binary algorithm for inversion in Fp")
        print("9. Partial Montgomery inversion in F_p")
        print("10. Chuyen 1 so ve dang mang")
        
        choice = int(input("Nhap lua chon: "))
        if choice == 1:
            
            w = int(input("Nhap w: "))
            p = int(input("Nhap p: "))
            m = math.ceil(math.log(p, 2))
            t = math.ceil(m/w)
            print("Nhap bieu dien mang cua a: ")
            for i in range (0, t): 
                x = int(input(f"a[{t - i - 1}] = "))
                arr_a.append(x)
            print("Nhap bieu dien mang cua b: ")
            for i in range (0, t): 
                x = int(input(f"b[{t - i - 1}] = "))
                arr_b.append(x)
                
            x = congTruongHH(arr_a, arr_b, t, w)
            print("Cong tren truong F_p ? 1. Co     2. Khong")      #In ra bieu dien tren truong F_p hay khong
            choice_cong = int(input("Nhap lua chon: "))
            while(choice_cong != 1 and choice_cong != 2):
                choice_cong = int(input("Input khong hop le, vui long thu lai: "))
            if choice_cong == 1:
                y = x[1]                                            #Lay ra bieu dien mang cua c = a + b
                y_val = 2**24 * y[0] + 2**16 * y[1] + 2**8 * y[2] + y[3]        # Tinh gia tri nguyen cua c
                if y_val >= p:                                      #Kiem tra xem co lon hon p hay khong
                    z = truTruongHH(y, bieuDienMang(p))
                    print(f"Bieu dien mang cua a + b tren truong F_p la: {z[1]}")
                else:
                    print(f"Bieu dien mang cua a + b tren truong F_p la {y}")
            else: 
                print(f"Bieu dien mang cua a + b tren truong huu han la: {x}")
                
                
        elif choice == 2:
            w = int(input("Nhap w: "))
            p = int(input("Nhap p: "))
            m = math.ceil(math.log(p, 2))
            t = math.ceil(m/w)
            print("Nhap bieu dien mang cua a: ")
            for i in range (0, t): 
                x = int(input(f"a[{t - i - 1}] = "))
                arr_a.append(x)
            print("Nhap bieu dien mang cua b: ")
            for i in range (0, t): 
                x = int(input(f"b[{t - i - 1}] = "))
                arr_b.append(x)
            
            
            x = truTruongHH(arr_a, arr_b, t, w)
            print("Tru tren truong F_p ? 1. Co     2. Khong")
            choice_tru = int(input("Nhap lua chon: "))
            while(choice_tru != 1 and choice_tru != 2):
                choice_tru = int(input("Input khong hop le, vui long thu lai: "))
            if choice_tru == 1:
                y = x[1]
                y_val = 2**24 * y[0] + 2**16 * y[1] + 2**8 * y[2] + y[3]
                if y_val >= p:
                    z = truTruongHH(y, bieuDienMang(p))
                    print(f"Bieu dien mang cua a - b tren truong F_p la: {z[1]}")
                else:
                    print(f"Bieu dien mang cua a - b tren truong F_p la {y}")
            if choice_tru == 2:
                print(f"Bieu dien mang cua a - b tren truong huu han la: {x}")  
                
        elif choice == 3:
            w = int(input("Nhap w: "))
            p = int(input("Nhap p: "))
            m = math.ceil(math.log(p, 2))
            t = math.ceil(m/w)
            print("Nhap bieu dien mang cua a: ")
            for i in range (0, t): 
                x = int(input(f"a[{t - i - 1}] = "))
                arr_a.append(x)
            print("Nhap bieu dien mang cua b: ")
            for i in range (0, t): 
                x = int(input(f"b[{t - i - 1}] = "))
                arr_b.append(x)
                
                
            c = nhan_operand(arr_a, arr_b, t, w)
            print(f"Bieu dien mang cua c = a.b la: {c[::-1]}")
            
        elif choice == 4: 
            p0 = int(input("Nhap p: "))
            b = int(input("Nhap b: "))
            k = math.floor(math.log(p0, b))
            z = int(input("Nhap z: "))
            while(z < 0 or z >= b**(2*k)):
                z = int(input("z khong hop le, vui long nhap lai: "))
            u0 = math.floor(b**(2*k)/p)
            r = luy_thua(p, b, k, z, u0)

        elif choice == 5: 
            a = int(input("Nhap a: "))
            b = int(input("Nhap b: "))
            uocChung = euclide_mo_rong(a, b)
            print(f"Bo so (d, x, y) doi voi a va b la: {uocChung}")
        elif choice == 6:
            
            p = int(input("Nhap so nguyen to p: "))
            while(checkPrime(p) == 0):
                p = int(input("p phai la mot so nguyen to, vui long nhap lai: "))
            a = int(input("Nhap a nam trong khoang [1, p-1]: "))
            while(a < 1 or a >= p):
                a = int(input("So vua nhap khong hop le, vui long thu lai: "))
            
            print(f"Nghich dao cua a module p (a^-1 mod p) la: {nghichDao(p, a)}")
        elif choice == 7: 
            a = int(input("Nhap a: "))
            b = int(input("Nhap b: "))
            print(f"Uoc chung lon nhat cua a va b la {Binary_gcd(a, b)}")
        elif choice == 8: 
            p = int(input("Nhap so nguyen to p: "))
            while(checkPrime(p) == 0):
                p = int(input("p phai la mot so nguyen to, vui long nhap lai: "))
            a = int(input("Nhap a nam trong khoang [1, p-1]: "))
            while(a < 1 or a >= p):
                a = int(input("So vua nhap khong hop le, vui long thu lai: "))
            print(f"Nghich dao cua a module p (a^-1 mod p) la: {BinaryInversionInFp(p, a)}")
        elif choice == 9: 
            p = int(input("Nhap so chan p > 2 : "))
            while (p <= 2 or p % 2 == 1):
                p = int(input("p phai lon hon 2 va la so chan, vui long nhap lai: "))
            a = int(input("Nhap a nam trong khoang [1, p-1]: "))
            while(a < 1 or a >= p):
                a = int(input("So vua nhap khong hop le, vui long thu lai: "))
            n = math.ceil(math.log(p, 2))
            partialMontInversionInFp(p, a, n)
            
        elif choice == 10:
            w = int(input("Nhap w: "))
            p = int(input("Nhap p: "))
            m = math.ceil(math.log(p, 2))
            t = math.ceil(m/w)
            a = int(input("Nhap so can chuyen: "))
            print(f"Bieu dien mang cua {a} la {bieuDienMang(a, w, t)}")
                
            