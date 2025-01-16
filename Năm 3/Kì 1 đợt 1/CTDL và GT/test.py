import math
primes = list(math.prime_range(3,117))
p = 4 * math.prod(primes) - 1 #Generate a prime
base = bytes((int(p).bit_length() + 7) // 8)
Fp = GF(p) #Create a galouis

def from_weierstrass(EC):
        a, b = EC.a4(), EC.a6()  #There are 2 forms that Y^2 +a1XY +a3Y = X^3 +a2 X^2 +a4X + a6
        F = EC.base_field()
        PR = PolynomialRing(F, name="z") #Create a polynomial ring with variable z
        z = PR.gens()[0]                #Choose z is the symbolic one
        roots = (z**3 + a*z + b).roots()    #Find roots
        assert len(roots) > 0               #Check if it has any roots
        alpha = roots[0][0]                 #Choose the first root
        s = (3*alpha**2 + a).sqrt() ** (-1)         # s * sqrt(3*alpha^2 + a) = 1
        return -3 * (-1)**s.is_square() * alpha * s 

def to_weierstrass(A):
        while True:
                B = Fp.random_element()
                if B.is_square() and B != 0:
                        break
        a = (3 - A**2) * pow(3 * B**2, -1, p)   # a = (3 - A^2)*((3*B^2)^-1 mod p) = 3 - ((3*B^2)^-1 mod p) when A = 0
        b = (2 * A**3 - 9 * A) * pow(27 * B**3, -1, p) # b = (2* A^3 - 9*A) * ((27*B^3)^-1 mod p) = 0 when A = 0
        return EllipticCurve(Fp, [a, b])

def group_action(pub, priv):
        es = priv.copy() 
        A = pub
        assert len(es) == len(primes)   #check if len(priv) == 27
        EC = to_weierstrass(A)          #Create elliptic curve EC from public key
        while True:
                if all(e == 0 for e in es): #if all e == 0 break
                        break
                x = Fp(randint(1, p-1))     #Choose x in range(1, p - 1)
                r = Fp(x ** 3 + A * x ** 2 + x)     #calculate Fp(x^3 + A*x^2 +x) then init r 
                s = kronecker_symbol(r, p)      #s is kronecker_symbol
                """
                A krocnecker_symbol for p primes is:
                r/p = 1 if r is a quadratic residue modulo p, a!= 0 mod p
                    = -1 if r is not 
                    = 0 if r == 0 mod p
                a quadratic residue modulo is the X^2 mod p with X in Fp(p) 
                """
                assert (2 * is_square(r)) - 1 == s      #Check if r square => s = 1 else s = -1
                I = [i for i, e in enumerate(es) if sign(e) == s]   #Store all index that e > 0 or e < 0 depends on s
                if len(I) == 0:         #There is no number deserves then generate again
                        continue    
                if s == -1:             
                        EC = EC.quadratic_twist()       #Create a quadratic twist
                while True:
                        tmp = EC.random_element()       #Choose a random point in EC
                        if not tmp.is_zero():           
                                break
                x = tmp.xy()[0]         #Take the x from tmp
                t = prod([primes[i] for i in I])
                P = EC.lift_x(x)        #Calculate the y or -y
                assert (p + 1) % t == 0     
                Q = ((p + 1) // t) * P      
                for i in I:
                        assert t % primes[i] == 0
                        R = (t // primes[i]) * Q
                        if R.is_zero():
                                continue
                        phi = EC.isogeny(R)
                        EC = phi.codomain()
                        Q = phi(Q)
                        assert t % primes[i] == 0
                        t = t // primes[i]
                        es[i] -= s
                if s == -1:
                        EC = EC.quadratic_twist()
        return from_weierstrass(EC)

def truncated(n, ratio):

        kbits = int(n.bit_length() * ratio)
        return (n >> kbits) << kbits

class CSIDH:

        def __init__(self):
                self.priv = [randint(-2, 2) for _ in primes]
                self.pub = group_action(0, self.priv)

        def getPublic(self):
                return self.pub

        def getShare(self, other):
                return group_action(other, self.priv)

Angel, Devil = CSIDH(), CSIDH()
print(f"Angel's Public Key = {Angel.getPublic()}")
print(f"Devil's Public Key = {Devil.getPublic()}")

choice = input("Deal with [A]ngel or [D]evil? Make your choice carefully: ")
if choice == "A":
        for i in range(5):
                A = int(input("Enter the montgomery coefficient: "))
                print(truncated(int(Angel.getShare(A)), 0.4))
elif choice == "D":
        for i in range(4):
                D = int(input("Enter the montgomery coefficient: "))
                print(truncated(int(Devil.getShare(D)), 0.3))
else:
        print("Ok ... You are from Super Guesser, right?")

S = int(Angel.getShare(Devil.getPublic()))
if int(input("Did Angel or Devil tell your the secret: ")) == S:
        try:
                f = open('flag.txt','r')
                FLAG = f.read()
                f.close()
        except:
                FLAG = "idek{debug}"
        print(f"FLAG = {FLAG}")
else:
        print("G_G")
"""
When we run, we will get A and D public key, which is group_action(0, private)
"""