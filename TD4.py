import matplotlib.pyplot as plt


class Hachtable:
    def __init__(self,n,h):
        self.size=n
        self.tableau=[[] for i in range(n)]
        self.hash=h


    def __str__(self):
        return str(self.tableau)


    def put(self,key,value):
        index=self.hash(key)%self.size
        (Bool,i)=search_key(self.tableau[index],key)
        if Bool==False:
            if cpt_el(self.tableau)>2*self.size:
                self.resize()
            self.tableau[index].append((key,value))
        else :
            self.tableau[index][i]=(key,value)

    def get(self,key):
        index=self.hash(key)%self.size
        (Bool,i)=search_key(self.tableau[index],key)
        if Bool:
            return self.tableau[index][i][1]
        else:
            return None

    def repartition(self):
        y=[len(self.tableau[i]) for i in range(self.size)]
        N = len(y)
        x = range(N)
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()


    def resize(self):
        new_size=2*self.size
        new_tableau=[[] for i in range(new_size)]
        for Sous_liste in self.tableau :
            for Duo in Sous_liste:
                key=Duo[0]
                value=Duo[1]
                index=self.hash(key)%new_size
                (Bool,i)=search_key(new_tableau[index],key)
                if Bool==False:
                    new_tableau[index].append((key,value))
                else :
                    new_tableau[index][i]=(key,value)
        self.tableau=new_tableau
        self.size=new_size



def cpt_el(L):
    cpt=0
    for Sous_liste in L :
        cpt+=len(Sous_liste)
    return cpt

def h1(s):
    h=sum([ord(c) for c in s])
    return h

def h2(s):
    h=0
    for c in s:
        h=h+31*h+ord(c)
    return h

def search_key(L,key):
    for i in range(len(L)):
        if L[i][0]==key:
            return (True,i)
    return (False,0)
























































