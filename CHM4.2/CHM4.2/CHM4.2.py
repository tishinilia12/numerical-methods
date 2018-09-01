hRead = open("F:\\test\\4.1\\14.txt", "r")
hWrite = open("F:\\test\\4.1\\ans14.txt","w")
import math
def fans1(x):
    return math.e**x-1
def f1(x,y,z):
    return z
def g1(x,y,z):
    return (2*z+math.e**x*y)/(math.e**x+1)
def K01(h,f,g,x,y,z):
    return h*(f(x,y,z))
def L01(h,f,g,x,y,z):
    return h*(g(x,y,z))
def K02(h,f,g,x,y,z):
    return h*(f(x+h/2,y+K01(h,f,g,x,y,z)/2,z+L01(h,f,g,x,y,z)/2))
def L02(h,f,g,x,y,z):
    return h*(g(x+h/2,y+K01(h,f,g,x,y,z)/2,z+L01(h,f,g,x,y,z)/2))
def K03(h,f,g,x,y,z):
    return h*(f(x+h/2,y+K02(h,f,g,x,y,z)/2,z+L02(h,f,g,x,y,z)/2))
def L03(h,f,g,x,y,z):
    return h*(g(x+h/2,y+K02(h,f,g,x,y,z)/2,z+L02(h,f,g,x,y,z)/2))
def K04(h,f,g,x,y,z):
    return h*(f(x+h,y+K03(h,f,g,x,y,z),z+L03(h,f,g,x,y,z)))
def L04(h,f,g,x,y,z):
    return h*(g(x+h,y+K03(h,f,g,x,y,z),z+L03(h,f,g,x,y,z)))
def metRK(h,f,g,x,y,z,Xend):
    k=0
    xm=[]
    ym=[]
    zm=[]
    while x<=Xend+h/10:
        dyk=Dy(h,f,g,x,y,z)
        dzk=Dz(h,f,g,x,y,z)
        yt=fans(x);
        zm.append(z);
        ym.append(y);
        xm.append(x);
        k+=1
        x+=h
        y+=dyk
        z+=dzk
    return xm,ym,zm
def metsho(h,f,g,x,y,z,X_):
    e=0.000001
    xmk=[]
    ymk=[]
    zmk=[]
    n=[]
    n.append(1)
    n.append(0.8)
    xm,ym,zm=metRK(h,f,g,x,y,n[0],X_)
    xmk.append(xm)
    ymk.append(ym)
    zmk.append(zm)
    xm,ym,zm=metRK(h,f,g,x,y,n[1],X_)
    xmk.append(xm)
    ymk.append(ym)
    zmk.append(zm)
    while(abs(zmk[-1][-1]-ymk[-1][-1]-1)>e):
        n.append(n[-1]-(n[-1]-n[-2])/(zmk[-1][-1]-zmk[-2][-1]))*zmk[-1][-1];
        xm,ym,zm=metRK(h,f,g,x,y,n[-1],X_)
        xmk.append(xm)
        ymk.append(ym)
        zmk.append(zm)
    return xm,ym,zm;
hRead.close()
hWrite.close()