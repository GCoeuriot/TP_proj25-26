import struct
import math
import numpy as np
import sys

def read_file(file):
    f=open(file,"rb")
    data=f.read()
    Left=[]
    Right=[]
    start=data.find(b"data")+len("data")
    size_data=struct.unpack_from("I",data,start)[0]
    for i in range(size_data//4):
        l,r=struct.unpack_from("hh",data,start+4+4*i)
        Left.append(l)
        Right.append(r)
    return Left,Right


def write_file(left,right,filename):
    with open(filename,"wb") as f:
        f.write(b"RIFF")
        f.write(struct.pack("I",44-8+len(left)*4))
        f.write(b"WAVEfmt ")
        f.write(struct.pack("IHHIIHH",16,1,2,44100,176400,4,16))
        f.write(b"data")
        f.write(struct.pack("I",len(left)*4))
        for i in range(len(left)):
            f.write(struct.pack("hh",left[i],right[i]))

def speed2(L):
    new=[]
    for i in range(len(L)//2):
        new.append(L[2*i])
    return new


def interpol(L):
    new=[]
    for i in range(len(L)-1):
        new.append(L[i])
        int=(L[i]+L[i+1])//2
        new.append(int)
    return new


def speedf(L,f):
    new=[]
    for i in range(int(len(L)/f)):
        new.append(L[int(f*i)])
    return new

def echo(duree,amplitude,L):
    new=L.copy()
    for i in range(duree,len(L)):
        new[i]=max(min(int(L[i]+L[i-duree]*amplitude),32767),-32768)
    return new







left,right=read_file("the_wall.wav")

write_file(left,right,"the_copy.wav")

lshort,rshort=speed2(left),speed2(right)
write_file(lshort,rshort,"high.wav")

linterpol,rinterpol=interpol(left),interpol(right)
write_file(linterpol,rinterpol,"interpol.wav")

lshortf,rshortf=speedf(left,3),speedf(right,3)
write_file(lshortf,rshortf,"speedf.wav")

lecho,recho=echo(len(left)*9//61,1/4,left),echo(len(right)*9//61,1/4,right)
write_file(lecho,recho,"echo.wav")

