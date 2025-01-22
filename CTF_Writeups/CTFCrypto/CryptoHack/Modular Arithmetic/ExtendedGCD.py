import math
def extendedGCD(a, b): 
    
    x2, x1, y2, y1 = 1, 0 , 0, 1
    q , r, x, y = 0, 0, 0 ,0
    while(True):
        q = math.floor(a / b)
        r = a % b
        a = b
        b = r
        x = x2 - q*x1
        y = y2 - q*y1
        x2 = x1 
        x1 = x
        y2 = y1
        y1 = y
        if b == 0: 
            return (x2, y2)

p, q = 26513, 32321
if p < q: 
    tmp = p
    p = q
    q = tmp
(u, v) = extendedGCD(p, q)
print((u, v))
print(p * u + q * v)