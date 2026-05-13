import tkinter as tk
import numpy as np
import random as rd

MARGIN=50
WIDTH=600
HEIGHT=600
K=0.6
L=100
M=30
DELTA_T=0.5


class App:
    def __init__(self,graph):
        self.graph=graph
        self.root=tk.Tk()
        self.canva=tk.Canvas(self.root,width=WIDTH,height=HEIGHT)
        self.canva.grid()
        self.root.bind('<f>',self.apply_force)
        self.redraw()


    def run_forever(self):
        self.root.mainloop()

    def redraw(self):
        self.canva.delete("all")
        self.draw_graph()

    def draw_graph(self):
        for i in range(self.graph.N) :
            self.draw_vertex(i)
        for (u,v) in self.graph.edges:
            self.draw_edge(u,v)


    def draw_edge(self,u,v):
        self.canva.create_line(self.graph.coordinates[u][0], self.graph.coordinates[u][1], self.graph.coordinates[v][0], self.graph.coordinates[v][1])

    def draw_vertex(self,u):
        x=self.graph.coordinates[u][0]
        y=self.graph.coordinates[u][1]
        self.canva.create_oval(x-4,y-4,x+4,y+4,fill="IndianRed1")

    def apply_force(self,_):
        self.graph.apply_force()
        self.redraw()


class Graph:
    def __init__(self,adj_list):
        self.N=len(adj_list)
        self.adj_list = adj_list
        self.edges=self.get_edges(adj_list)
        self.coordinates=np.array([(rd.randint(MARGIN,WIDTH-MARGIN),rd.randint(MARGIN,HEIGHT-MARGIN)) for i in range(self.N)])
        self.speeds=np.array([((rd.random()-0.5)*10, (rd.random()-0.5)*10) for i in range(self.N)])



    def get_edges(self,adj_list):
        L=[]
        for i in range(len(adj_list)):
            for e in adj_list[i]:
                L.append((i,e))
        return L


    def apply_force(self,):
        force=np.zeros((self.N,2))
        for e in self.edges:
            u=e[0]
            v=e[1]
            vecteur=[self.coordinates[v][0]-self.coordinates[u][0],self.coordinates[v][1]-self.coordinates[u][1]]
            d=(vecteur[0]**2+vecteur[1]**2)**(1/2)
            vecteur_norm=vecteur/d
            force[u]+=K*(d-L)*vecteur_norm
            force[v]+=-K*(d-L)*vecteur_norm

        for i in range(self.N):
            self.speeds[i]=force[i]*DELTA_T/M + self.speeds[i]
            self.coordinates[i]=self.coordinates[i]+self.speeds[i]*DELTA_T


if __name__=="__main__":
    graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
    graphe=Graph(graph)
    app=App(graphe)
    app.run_forever()





















