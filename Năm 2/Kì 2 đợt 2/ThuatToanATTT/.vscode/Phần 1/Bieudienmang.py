import math
p = int(input("Nhap p: "))
w = int(input("Nhap w: "))
a = int(input("Nhap a: "))
m = math.ceil(math.log(p, 2))
t = math.ceil(m/w)
array_a = []
while(t > 0):
    x = 2**(w*(t - 1))
    array_a.append(int(a/x))
    a -= int(a/x)*x
    t -= 1
print(f"Bieu dien mang cua a tren truong F_{p} voi W = {w} la: ")
print(array_a)