from typing import List

class GFElement:
    def __init__(self, coeffs: List[int], p: int, mod_poly: List[int]):
       
        self.p = p
        self.mod_poly = mod_poly
        self.coeffs = [c % p for c in coeffs]
        self.reduce()

    def reduce(self):
      
        deg_mod = len(self.mod_poly) - 1
        coeffs = self.coeffs[:]
        while len(coeffs) >= len(self.mod_poly):
            if coeffs[-1] != 0:
               
                factor = coeffs[-1]
                for i in range(len(self.mod_poly)):
                    coeffs[-len(self.mod_poly)+i] = (coeffs[-len(self.mod_poly)+i] - factor * self.mod_poly[i]) % self.p
            coeffs.pop() 
        self.coeffs = coeffs

    def __add__(self, other):
       
        max_len = max(len(self.coeffs), len(other.coeffs))
        a = self.coeffs + [0]*(max_len-len(self.coeffs))
        b = other.coeffs + [0]*(max_len-len(other.coeffs))
        return GFElement([ (x+y)%self.p for x,y in zip(a,b) ], self.p, self.mod_poly)

    def __sub__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        a = self.coeffs + [0]*(max_len-len(self.coeffs))
        b = other.coeffs + [0]*(max_len-len(other.coeffs))
        return GFElement([ (x-y)%self.p for x,y in zip(a,b) ], self.p, self.mod_poly)

    def __mul__(self, other):
       
        a = self.coeffs
        b = other.coeffs
        res = [0]*(len(a)+len(b)-1)
        for i in range(len(a)):
            for j in range(len(b)):
                res[i+j] = (res[i+j] + a[i]*b[j]) % self.p
        return GFElement(res, self.p, self.mod_poly)

    def __eq__(self, other):
        return self.coeffs == other.coeffs and self.p == other.p and self.mod_poly == other.mod_poly

    def __repr__(self):
        return f"{self.coeffs} in GF({self.p}^{len(self.mod_poly)-1})"

   
    def inverse(self):
        
        def poly_divmod(a, b):
            """返回 q,r 使得 a = q*b + r"""
            a = a[:]
            deg_b = len(b)-1
            deg_a = len(a)-1
            q = [0]*(deg_a - deg_b + 1)
            while deg_a >= deg_b:
                factor = a[-1] * pow(b[-1], -1, self.p) % self.p
                q[deg_a - deg_b] = factor
                for i in range(deg_b+1):
                    a[deg_a - deg_b + i] = (a[deg_a - deg_b + i] - factor*b[i]) % self.p
                while a and a[-1]==0:
                    a.pop()
                deg_a = len(a)-1
            return q, a

        def egcd(a, b):
            """擴展歐幾里得算法多項式版"""
            x0, x1 = [1], [0]
            y0, y1 = [0], [1]
            while b:
                q, r = poly_divmod(a, b)
                a, b = b, r
                x0, x1 = x1, [(x0[i] - (q[i] if i<len(q) else 0)*x1[i])%self.p for i in range(max(len(x0),len(x1)))]
                y0, y1 = y1, [(y0[i] - (q[i] if i<len(q) else 0)*y1[i])%self.p for i in range(max(len(y0),len(y1)))]
            return a, x0, y0

        gcd, x, y = egcd(self.mod_poly, self.coeffs)
        if gcd != [1]:
            raise ValueError("無逆元")
        return GFElement(y, self.p, self.mod_poly)
//https://chatgpt.com/share/695a0c72-02c0-8004-ab28-37247e194b87