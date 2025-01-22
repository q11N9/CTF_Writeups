def gcd(x, y):
    if y == 0: 
        return x
    return gcd(y, x % y)
a, b = 32321, 26513
print(gcd(a, b))