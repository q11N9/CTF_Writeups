#KMP algorithm 
def failure_function(j, p):
    if j == 0:
        return -1
    if j == 1:
        return 0
    if j >= 2:
        prefixes = []
        suffixes = []
        for m in range(1, j + 1):           #Tim tat ca cac prefixes
            prefixes.append(p[0:m]) 
        for m in range(1, j):
            suffixes.append(p[m:j])
        set1 = set(prefixes)
        set2 = set(suffixes)
        intersection = set1.intersection(set2)      #Tim cac phan tu chung giua 2 prefix and suffix
        if len(intersection) == 0:
            return 0
        return max(len(i) for i in intersection)
def looking_glass(t, p, i, j):
    while t[i + j] == p[j]:
        if j == len(p) - 1:
            return [i, j]       #Neu j = len(p) - 1 thi return tim duoc chuoi o vi tri x
        j += 1
    return [i, j]
def jump(t, i, j, p):
    f_j = failure_function(j, p)
    i += j - f_j
    if f_j == -1:
        j = 0
    else:
        j = f_j
    return [i, j]
def kmp(t, p):
    n = len(t)
    m = len(p)
    if n < m:           #Neu p co do dai hon t thi khong ton tai
        return -1  
    if m == 0:          #Mang trong thi luon luon tim thay
        return 0  
    i = 0
    j = 0
    while i < n:
        if t[i + j] == p[j]:
            lg = looking_glass(t, p, i, j)
            i = lg[0]
            j = lg[1]
            if j == m - 1 and t[i + j] == p[j]:
                return i
        else:
            character_jump = jump(t, i, j, p)
            print(f"F({j}) = {failure_function(j, p)}")
            i = character_jump[0]
            j = character_jump[1]
        print(f"i = {i}, j = {j}")
    return -1

t = input("Nhap t: ")
p = input("Nhap p: ")
print("Chuoi p tim duoc o vi tri: ", kmp(t, p))