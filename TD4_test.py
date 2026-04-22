from TD4 import Hachtable
from time import perf_counter

f=open("frenchssaccent.dic","r")
T1=Hachtable(320,h1)
lexique=[]
for ligne in f:
    lexique.append(ligne[:len(ligne)-1])
start = perf_counter()
for el in lexique:
    T1.put(el, len(el))
end = perf_counter()
print((end-start)/len(lexique))
print(T1.repartition())