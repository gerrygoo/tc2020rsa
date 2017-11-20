#do rsa proyect here
from math import gcd
import random
class RSA:

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.N = p*q
        self.ϕ = self.ϕ_primes(p, q)

        self.e = self.e_pq(p, q)
        self.d = self.d_pq(p, q, self.e)

        self.public_key = (self.e, self.N)
        self.private_key = (self.d, self.N)

    def encrypt(self, m):
        return self.encrypted(m, self.e, self.N)

    def decrypt(self, c):
        return self.decrypted(c, self.d, self.N)
    
    @classmethod
    def xgcd(cls, a, b):
        x = 0
        y = 1
        lx = 1
        ly = 0
        oa = a 
        ob = b
        while b != 0:
            q = a // b
            (a, b) = (b, a % b)
            (x, lx) = ((lx - (q * x)), x)
            (y, ly) = ((ly - (q * y)), y)
        if lx < 0:
            lx += ob
        if ly < 0:
            ly += oa  
        # return a , lx, ly
        return lx

    @classmethod
    def ϕ_primes(cls, p, q): return (p - 1) * (q - 1)

    @classmethod
    def e_pq(cls, p, q):
        ϕ = cls.ϕ_primes(p, q)

        e = random.randrange(1, ϕ)
        g = gcd(e, ϕ)
        while g != 1:
            e = random.randrange(1, ϕ)
            g = gcd(e, ϕ)
        return e
    
    @classmethod
    def d_pq(cls, p, q, e):
        # return cls.xgcd(cls.ϕ_primes(p, q), e)
        return cls.xgcd(e, cls.ϕ_primes(p, q))

    @classmethod
    def encrypted(cls, m, e, N):
        return (m ** e) % N
    
    @classmethod
    def decrypted(cls, c, d, N):
        return (c ** d) % N

    
