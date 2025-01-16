def soUocNguyenTo(N):
    soUocNguyenTo = 0
    i = 2
    while(1):
        if (N == 1): 
            break
        if (N % i != 0):
            i+=1
        if (N % i == 0):
            soUocNguyenTo += 1
            while(N % i == 0):
                N /= i
    return soUocNguyenTo  
              
def tongUocNguyenTo(N):
    sum = 0
    i = 2
    while(1):
        if (N == 1): 
            break
        if (N % i != 0):
            i+=1
            
        if (N % i == 0):
            sum += i
            while(N % i == 0):
                N /= i
    return sum
def tinhSoUoc(N):
    soUoc = 1
    for i in range (1, int(N/2) + 1):
        if N % i == 0: 
            soUoc+=1
    return soUoc
def tinhTongCacUoc(N):
    for i in range(1, int(N/2)+1):
        if N%i == 0:
            N+=i
    return N
N = int(input("Nhap N: "))
print(tongUocNguyenTo(N))