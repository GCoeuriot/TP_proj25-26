tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']

###exo 2

f=open("frenchssaccent.dic","r")
lexique=[]
for ligne in f:
    lexique.append(ligne[:len(ligne)-1])

def plus_long(L,dico):
    long=0
    plus_long=[]
    for mot in dico :
        if len(mot)>long:
            L_test=L.copy()
            if ecrivable(mot,L_test)==True:
                plus_long=mot
                long=len(mot)
    return plus_long,long

def ecrivable(mot,L):
    for i in range(len(mot)):
        if mot[i] not in L:
            return False
        else :
            ind=recherche_lettre(mot[i],L)
            L.pop(ind)
    return True

def recherche_lettre(a,L):
    cpt=0
    for i in range(len(L)):
        if L[i]==a:
            return i
    return False

###exo 3

def points(str):
    if str in ["a","e","i","l","n","o","r","s","t","u"]:
        return 1
    elif str in ["d","g","m"]:
        return 2
    elif str in ["b","c","p"]:
        return 3
    elif str in ["f","h","v"]:
        return 4
    elif str in ["j","q"]:
        return 8
    elif str in ["k","w","x","y","z"]:
        return 10

def score(str):
    cpt=0
    for i in str:
        cpt+=points(i)
    return cpt

def plus_points(L,dico):
    points=0
    plus_points=[]
    for mot in dico :
        if score(mot)>points:
            L_test=L.copy()
            if ecrivable(mot,L_test)==True:
                plus_points=mot
                points=score(mot)
    return plus_points,points

###exo 4

def points(str):
    if str in ["a","e","i","l","n","o","r","s","t","u"]:
        return 1
    elif str in ["d","g","m"]:
        return 2
    elif str in ["b","c","p"]:
        return 3
    elif str in ["f","h","v"]:
        return 4
    elif str in ["j","q"]:
        return 8
    elif str in ["k","w","x","y","z"]:
        return 10
    elif str=='?':
        return 0


def remplacement_joker(lettre,L):
    nouv_mot=[]
    for i in range(len(L)):
        if L[i]!='?':
            nouv_mot+=L[i]
        if L[i]=='?':
            nouv_mot+=lettre
        print(nouv_mot)
    return nouv_mot

def plus_points_jok(L,dico):
    points=0
    plus_points=[]
    if '?' not in L:
        for mot in dico :
            if score(mot)>points:
                L_test=L.copy()
                if ecrivable(mot,L_test)==True:
                    plus_points=mot
                    points=score(mot)
        return plus_points,points
    else :
        for mot in dico :
            alphabet=["a","e","i","l","n","o","r","s","t","u","d","g","m","b","c","p","f","h","v","j","q","k","w","x","y","z"]
            for lettre in alphabet:
                mot_nouv=remplacement_joker(lettre,L)
                if score(mot)-points(lettre)>points:
                    L_test=L.copy()
                    if ecrivable(mot,L_test)==True:
                        plus_points=mot
                        points=score(mot)
        return plus_points,points





