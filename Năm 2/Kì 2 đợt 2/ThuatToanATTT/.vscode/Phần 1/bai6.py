import math
def tongUocSo(N):
    sum = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            sum += i
            if i != N // i:
                sum += N // i
        i += 1
    return sum - N

if __name__ == "__main__":
    N = int(input("Nhap N: "))
    res = []
    for i in range (1, N):
        x = tongUocSo(i)
        if x < N:
            res.append([i, x])
    if len(res) == 0:
        print("Khong co cap so than thiet nao nho hon N")
    else:
        print(f"Cac cap so than thiet nho hon N la: {res}")