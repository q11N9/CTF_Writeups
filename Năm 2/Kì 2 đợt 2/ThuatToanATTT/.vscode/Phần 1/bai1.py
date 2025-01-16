import math
def isQPrime(q):
    uoc = 2
    for i in range(2, q):
        if q % i == 0: 
            uoc += 1
        if uoc > 4: 
            return 0 
    return uoc == 4

if __name__ == "__main__":
    n = int(input("Nhap N: "))
    if n < 6:
        print("Khong co so Q-prime nao")
    else: 
        count = 0
        for i in range (6, n+1):
            if isQPrime(i) == 1: 
                count += 1
                if count == 1:
                    print("Cac so Q-prime nho hon hoac bang N la")
                print(f"{i:-10d}",end="")
                if count > 0 and count % 5 == 0:
                    print("")
        if count == 0:
            print("Khong co so Q-prime nao nho hon hoac bang N")
