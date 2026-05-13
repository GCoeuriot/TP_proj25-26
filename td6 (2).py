import tkinter as tk
import random as rd

Min_croisements=10
Max_croisements=20
Max_fil=9
Min_fil=3



class App:
    def __init__(self,data):
        self.data=data
        self.color=["blue","red","green","purple","yellow","orange","black","blue","brown"]
        self.root=tk.Tk()
        self.canva=tk.Canvas(self.root,width=2*self.data.w*len(self.data.Croisements)+self.data.w, height=(self.data.h+10)*self.data.n)
        self.canva.grid()
        self.b1=tk.Button(self.root,text='Quit',command=self.root.destroy,bg='grey',)
        self.b2=tk.Button(self.root,text='Colors',command=self.redraw,bg='grey')
        self.b3=tk.Button(self.root,text='Random',command=self.random,bg='grey')
        self.l=tk.Label(self.root,text='Croisement'+'   '+ str(self.data.Croisements))
        self.b1.grid(column=0,row=2)
        self.b2.grid(column=1,row=2)
        self.b3.grid(column=2,row=2)
        self.l.grid(column=0,row=1)
        self.affichage()
        self.redraw()
        self.affichage()
        self.root.bind('<Button-1>',self.reidmeister)


    def redraw(self):
        rd.shuffle(self.color)
        self.canva.delete("all")
        self.affichage()

    def read_word(self,mot,x0,y0,color):
        x=x0
        y=y0
        for e in mot :
            if e=='H':
                self.canva.create_line(x,y,x+self.data.w,y,fill=color)
                x+=self.data.w
            elif e=='U':
                self.canva.create_line(x,y,x+self.data.w,y+self.data.h,fill=color)
                x+=self.data.w
                y+=self.data.h
            elif e=='D':
                self.canva.create_line(x,y,x+self.data.w,y-self.data.h,fill=color)
                x+=self.data.w
                y-=self.data.h

    def run_forever(self):
        self.root.mainloop()

    def affichage(self):
        D=data.entrelacs()
        for i in range(len(D)):
            self.read_word(D[i],0,i*self.data.h+50,self.color[i])

    def random(self):
        self.data.n=rd.randint(Min_fil,Max_fil)
        nb_croisements=rd.randint(Min_croisements,Max_croisements)
        self.data.Croisements=[rd.randint(0,self.data.n-2) for i in range(nb_croisements)]
        self.root.destroy()
        self.__init__(data)

    def reidmeister(self,event):
        X = event.x_root
        Y = event.y_root
        print(X,Y)




class Data:

    def __init__(self,n,Croisements,w,h):
        self.n=n
        self.Croisements=Croisements
        self.w=w
        self.h=h

    def entrelacs(self):
        D={i :'H' for i in range(self.n)}
        Incidence=[i for i in range(self.n)]
        for e in self.Croisements:
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






if __name__=="__main__":
    data=Data(7,[2,1,1,0,2],20,20)
    app=App(data)
    app.run_forever()









