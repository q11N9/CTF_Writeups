import math
def bieuDienMang(a, w, t):
    arr = []
    while t > 0:
        x = 2**(w*(t - 1))
        arr.append(int(a/x))
        a -= int(a/x)*x
        t -= 1
    return arr

def cong(a, b, t, w):
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

def bieuDienNguyen(arr, w, t):
    x = 0
    i = 0
    while t > 0:
        r = 2**(w*(t - 1))
        x += arr[i] * r
        t -= 1
        i += 1
    return x
if __name__ == "__main__":
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    p = int(input("Nhap so nguyen to p: "))
    w = int(input("Nhap w: "))
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m/w)
    arr_a = bieuDienMang(a,w,t)
    arr_b = bieuDienMang(b, w, t)
    print(f"Bieu dien mang cua a = {a} la: {arr_a}")
    print(f"Bieu dien mang cua b = {b} la: {arr_b}")
    x = cong(arr_a, arr_b, t, w)
    print(f"Bieu dien mang cua a + b la {x[1]} va dang so nguyen cua no la: {bieuDienNguyen(x[1], w, t)}")
    