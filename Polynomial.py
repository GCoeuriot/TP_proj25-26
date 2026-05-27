import numpy as np
import random as rd



class PolyMod:
    def __init__(self,coef,q,n):
        self.coefs=coef
        self.q=q
        self.n=n

    def __str__(self):
            terms = []
            for i in range(len(self.coefs) - 1, -1, -1):  # Parcourir les coefficients en ordre décroissant
                coef = self.coefs[i]
                if coef == 0:  # Ignorer les coefficients nuls
                    continue
                if i == 0:  # Terme constant
                    terms.append(f"{coef}")
                elif i == 1:  # Terme de degré 1
                    if coef == 1:
                        terms.append("X")
                    elif coef == -1:
                        terms.append("-X")
                    else:
                        terms.append(f"{coef}*X")
                else:  # Terme de degré supérieur
                    if coef == 1:
                        terms.append(f"X^{i}")
                    elif coef == -1:
                        terms.append(f"-X^{i}")
                    else:
                        terms.append(f"{coef}*X^{i}")
            if len(terms) == 0:  # Si tous les coefficients sont nuls
                return "0"
            # Joindre les termes avec le bon signe
            res = " + ".join(terms)
            return res.replace("+ -", "- ")

    def scalar(self,c):
        new_coefs=[(ai*c) % self.q for ai in self.coefs]
        return PolyMod(new_coefs,self.q,self.n)

    def rescale(self,r):
        new_coefs=[ai % r for ai in self.coefs]
        return PolyMod(new_coefs,r,self.n)

    def degre(self):
        return len(self.coefs)-1

    def __add__(self,other):
        if self.q==other.q and self.n==other.n :
            coef_add=[(self.coefs[i] + other.coefs[i]) % self.q for i in range(self.degre()+1)]
            return PolyMod(coef_add,self.q,self.n)
        else :
            print("impossible")

    def __mul__(self, other):
            if self.q != other.q or self.n != other.n:
                print("Erreur : q ou n différents, multiplication impossible dans ce corps.")
                return None
            deg_self = self.degre()
            deg_other = other.degre()
            deg_prod = deg_self + deg_other
            coef_mul = [0] * (deg_prod + 1)
            for k in range(deg_prod + 1):
                ck = 0
                start_j = max(0, k - deg_other)
                end_j = min(k, deg_self)
                for j in range(start_j, end_j + 1):
                    ck += self.coefs[j] * other.coefs[k - j]
                coef_mul[k] = ck % self.q
            return PolyMod(coef_mul, self.q, self.n)

    def fscalar(self,r,alpha):
        new_coefs=[round(self.coef[i]*alpha)%r for i in range(self.n)]
        return PolyMod(new_coefs,self.q,self.n)

    def gen_uniform_random(q,n,a,b):
        new_coefs=[rd.randint(a,b) for _ in range(n)]
        return PolyMod(new_coefs,q,n)

    def congruence(self):
        return self.q

    def crypt(self,p,pk):
        (b,a)=pk
        t=p.congruence()
        q=a.congruence()
        delta=q/t
        sp=p.scalar(delta)
        u=gen_uniform_random(0,1)
        e1=gen_uniform_random(-1,1)
        x1=b.mul(u)
        y1=x1.add(e1)
        c1=y1.add(sp)
        e2=gen_uniform_random(-1,1)
        x2=a.mul(u)
        c2=x2.add(e2)
        return (c1,c2)

class EncryptedPoly:

    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2

    def decrypt(self,key,t):
        a=self.c2.mul(key)
        b=a.add(self.c1)
        q=a.congruence()
        c=b.fscalar(t/q,t)




