p = 29
ints = [14,6,11]
for i in ints:
    for j in range(29):
        if (j * j) % p == i:
            print("Square root of " + str(i) + " is " + str(j) )