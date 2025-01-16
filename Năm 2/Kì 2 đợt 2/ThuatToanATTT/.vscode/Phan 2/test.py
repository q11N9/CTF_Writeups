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
print(nhanBinhPhuong(2, 757, 607))