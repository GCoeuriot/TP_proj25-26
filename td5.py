import tkinter as tk
import random as rd

color=["blue","red","green","purple","yellow","orange","beige"]
Croisements=[2,1,1,0,2]
n=7
w=20
h=20


def read_word(canvas, mot, h, w,x0,y0,color):
    x=x0
    y=y0
    for e in mot :
        if e=='H':
            canvas.create_line(x,y,x+w,y,fill=color)
            x+=w
        elif e=='U':
            canvas.create_line(x,y,x+w,y+h,fill=color)
            x+=w
            y+=h
        elif e=='D':
            canvas.create_line(x,y,x+w,y-h,fill=color)
            x+=w
            y-=h


def entrelacs(L,n):
    D={i :'H' for i in range(n)}
    Incidence=[i for i in range(n)]
    for e in L:
        fil1=e
        fil2=e+1
        D[Incidence[fil1]]+='U'
        D[Incidence[fil2]]+='D'
        a=Incidence[fil1]
        b=Incidence[fil2]
        Incidence[fil1]=b
        Incidence[fil2]=a
        for key in D.keys():
            if key!= Incidence[fil1] and key != Incidence[fil2]:
                D[key]+='H'
        for key in D.keys():
            D[key]+='H'
    return D

def recherche(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return i

def change_couleurs():
    rd.shuffle(color)
    c.delete("all")
    affichage(Croisements,n)

def affichage(Croisements,n):
    D=entrelacs(Croisements,n)
    for i in range(len(D)):
        read_word(c,D[i],h,w,0,i*h+50,color[i])

root=tk.Tk()
c=tk.Canvas(root,width=2*w*len(Croisements)+w, height=(h+10)*n)
c.grid()

b1=tk.Button(root,text='Quit',command=root.destroy,bg='grey',)
b2=tk.Button(root,text='Colors',command=change_couleurs,bg='grey')
l=tk.Label(root,text='Croisement'+'   '+ str(Croisements))
b1.grid(column=0,row=2)
b2.grid(column=1,row=2)
l.grid(column=0,row=1)

affichage(Croisements,n)


root.mainloop()