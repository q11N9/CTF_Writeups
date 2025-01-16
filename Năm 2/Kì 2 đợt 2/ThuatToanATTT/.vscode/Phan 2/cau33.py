# Can use galois to calculate
def rutgonMang(a):
    for i in range(len(a) - 1, -1, -1): 
        if a[i] == 1:
            break
        else:
            a.pop()

def phepCong(a, b):
    rutgonMang(a)
    rutgonMang(b)
    if len(b) == 0:
        return a.copy()
    if len(a) == 0:
        return b.copy()
    len_a = len(a)
    len_b = len(b)
    c = []
    for i in range(0, min(len_a, len_b)):
        if a[i] == b[i]:
            c.append(0)
        else:
            c.append(1)
    while len(c) < len(a):
        for i in range(len(c), len(a)):
            c.append(a[i])
    while len(c) < len(b):
        for i in range(len(c), len(b)):
            c.append(b[i])
    return c.copy()

def phepNhan(a, b):
    rutgonMang(a)
    rutgonMang(b)
    c = []
    if len(b) == 0:
        return []
    if len(b) == 1:
        return a.copy()
    if len(a) == 1:
        return b.copy()
    for i in range(0, len(a)):
        if a[i] == 0:
            continue
        else:
            r = []
            for j in range(0, len(b)):
                r.append(b[j])
            k = i
            while k != 0:
                r.insert(0, 0)      #Dich 1 vi tri so voi ban dau, vi du nhu x*[1, 1, 0] = [0, 1, 1, 0]
                k -= 1
            c = phepCong(c, r)
    return c.copy()
def layModule(a, b, q):
    rutgonMang(a)
    if len(a) == 0:           #Neu so bi chia bang 0 thi return
        return [[], []]
    if len(b) == 1:
        return [a.copy(), []]
    if len(a) < len(b):                                 #Neu bac cua so bi chia nho hon thi return
        return [q, a.copy()]
    else:
        bac_a = len(a) - 1
        bac_b = len(b) - 1
        thuong = [1]
        bac_thuong = bac_a - bac_b
        while bac_thuong > 0:
            thuong.insert(0,0)
            bac_thuong -= 1
        q = phepCong(q, thuong)
        a = phepCong(a, phepNhan(b, thuong))
        return layModule(a, b, q)

def extendedEuclide(a, b): 
    g = a.copy()
    x2, x1, y2, y1 = [1], [], [], [1]
    print("q       r        x       y       a       b       x2      x1      y2      y1")
    while 1:
        if len(b) == 0:
            break
        thuong = []
        z = layModule(a.copy(), b.copy(), thuong)
        q = z[0]
        r = z[1]
        qx1 = phepNhan(q, x1)
        x = phepCong(x2, layModule(qx1, g, [])[1])
        qy1 = phepNhan(q, y1)
        y = phepCong(y2, layModule(qy1, g, [])[1])
        a = b.copy()
        b = r.copy()
        
        x2 = x1.copy()
        x1 = x.copy()
        y2 = y1.copy()
        y1 = y.copy()
        print(f"{q}  {r}  {x}  {y}  {a}  {b}  {x2}  {x1}  {y2}  {y1}")
    return (a, x2,y2)
        
if __name__ == "__main__":
    a = input("Nhap a: ")
    print("Nhap a: ")
    arr_a = []
    for _ in range(len(a) - 1, -1, -1):
        x = int(a[_])
        arr_a.append(x)
    print(arr_a)
    g = input("Nhap g: ")
    arr_g = []
    for _ in range(len(g) - 1, -1, -1):
        x = int(g[_])
        arr_g.append(x)
    print(arr_g)
    res = extendedEuclide(arr_g, arr_a)
    print(res)
    inverse_a = res[2]
    print("a^-1(x) = ", end="")
    terms = []

    for i in range(len(inverse_a)):
        if inverse_a[i] == 1:
            if i == 0:
                terms.append("1")
            elif i == 1:
                terms.append("x")
            else:
                terms.append(f"x^{i}")
    if terms:
        print(" + ".join(terms))
    else:
        print("0")
