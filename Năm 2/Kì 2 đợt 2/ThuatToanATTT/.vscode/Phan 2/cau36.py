def last_occurrence(p):
    l_x = [-1] * 128  
    for i in range(len(p)):
        l_x[ord(p[i])] = i          #Khi chay den cuoi, gia tri l_x[ord(p[i])] se cho ra index lon nhat cua p[i]
    return l_x

def looking_glass(t, p, i, j):
    while t[i] == p[j]:
        if j == 0:
            return [i, j]       #Neu j = 0 thi return tim duoc chuoi o vi tri i
        i -= 1
        j -= 1
    return [i, j]

def character_jump(t, i, j, m, l_x):
    shift = min(j, 1 + l_x[ord(t[i])])
    i += m - shift
    j = m - 1
    return [i, j]
def inBangTienXuLy(l_x, p):
    different_char = set(p)
    print("x      ", end="")
    for char in different_char:
        print(f"{char}   ", end="")
    print("*\nL(x)   ", end = "")
    for char in different_char:
        print(f"{l_x[ord(char)]}   ", end="")
    print("-1")
def boyer_moore(t, p):
    n = len(t)
    m = len(p)
    if n < m:           #Neu p co do dai hon t thi khong ton tai
        return -1  
    if m == 0:          #Mang trong thi luon luon tim thay
        return 0  

    l_x = last_occurrence(p)

    i = m - 1
    j = m - 1
    while i < n:
        if t[i] == p[j]:
            lg = looking_glass(t, p, i, j)
            i = lg[0]
            j = lg[1]
            if j == 0:  
                return i
        else:
            cj = character_jump(t, i, j, m, l_x)
            i = cj[0]
            j = cj[1]
            if i > n: 
                break
            shift =  min(j, 1 + l_x[ord(t[i])])
            print(f"Min = {shift}")
        print(f"i = {i}, j = {j}")
    return -1  #Khong tim thay p trong t

text = input("Nhap t: ")
pattern = input("Nhap p: ")
index = boyer_moore(text, pattern)
if index == -1:
    print("Khong tim duoc vi tri cua chuoi p trong t")
else:
    print("Chuoi p tim duoc o vi tri:", index)
