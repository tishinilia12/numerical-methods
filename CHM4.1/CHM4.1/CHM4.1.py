hRead = open("F:\\test\\4.1\\14.txt", "r")
hWrite = open("F:\\test\\4.1\\ans14.txt","w")
import math
def fans2(x):
    return x**3+3*x+1
def f2(x,y,z):
    return z;
def g2(x,y,z):
    return (2*x*z)/(x*x+1)
def fans1(x):
    return (-0.9783*math.cos(2*x)+0.4776*math.sin(2*x))/(math.sin(1*x))
def f1(x,y,z):
    return z;
def g1(x,y,z):
    return -2*z*(1/math.tan(x))-3*y
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
def Dy(h,f,g,x,y,z):
    return (K01(h,f,g,x,y,z)+2*K02(h,f,g,x,y,z)+2*K03(h,f,g,x,y,z)+K04(h,f,g,x,y,z))/6
def Dz(h,f,g,x,y,z):
    return (L01(h,f,g,x,y,z)+2*L02(h,f,g,x,y,z)+2*L03(h,f,g,x,y,z)+L04(h,f,g,x,y,z))/6
def euler_method(h,f,g,x,y,z,fans,Xend):
    k=0
    hWrite.write("Метод Эйлера\n")
    hWrite.write("  k  xk    yk             zk             yист           Ek\n");
    xm=[]
    ym=[]
    zm=[]
    while x<=Xend+h/10:
        yNext = y + h * f(x,y,z)
        zNext = z + h * g(x, y,z)
        yt=fans(x);
        e=abs(y-yt)
        zm.append(z);
        ym.append(y);
        xm.append(x);
        hWrite.write("{:3d}{:5.1f}{:15.10f}{:15.10f}{:15.10f}{:15.10f}\n".\
            format(k,x,y,z,yt,e));
        k+=1
        x+=h
        y=yNext
        z=zNext
    return xm,ym,zm
def mod_euler_method(h,f,g,x,y,z,fans,Xend):
    k=0
    hWrite.write("Метод Эйлера(мод)\n")
    hWrite.write("  k  xk    yk             zk             yист           Ek\n");
    xm=[]
    ym=[]
    zm=[]
    while x<=Xend+h/10:
        x_half = x + h/2;
        y_half = y + h/2 * z;
        dy_half = z + h/2 * g(x, y, z);
        yNext = y + h * dy_half;
        zNext = z + h * g(x_half, y_half, dy_half);
        yt=fans(x);
        e=abs(y-yt)
        zm.append(z);
        ym.append(y);
        xm.append(x);
        hWrite.write("{:3d}{:5.1f}{:15.10f}{:15.10f}{:15.10f}{:15.10f}\n".\
            format(k,x,y,z,yt,e));
        k+=1
        x+=h
        y=yNext
        z=zNext
    return xm,ym,zm
def adams_itearation(f,x,y,z,i):
    return (55. * f(x[i-1],y[i-1],z[i-1])-59. * f(x[i-2],y[i-2],z[i-2]) +37. * f(x[i-3],y[i-3],z[i-3]) -9. * f(x[i-4],y[i-4],z[i-4])) / 24.;
def adams_method(h,f,g,fans,xm,ym,zm):
    x=[i for i in xm]
    y=[i for i in ym]
    z=[i for i in zm]
    if len(ym)<4 or len(zm)<4:
        print("ошибка для метода Адама")
    hWrite.write("метода Адама\n")
    hWrite.write("  k  xk    yk             zk             yист           Ek\n");
    for i in range(4,len(xm)):
        y[i]= y[i-1] + h * adams_itearation(f, x, y, z, i);
        z[i] = z[i-1] + h * adams_itearation(g, x, y, z, i);
        yt=fans(x[i]);
        e=abs(y[i]-yt)
        hWrite.write("{:3d}{:5.1f}{:15.10f}{:15.10f}{:15.10f}{:15.10f}\n".\
            format(i,x[i],y[i],z[i],yt,e));
    return x,y,z;
def metRK(h,f,g,x,y,z,fans,Xend):
    k=0
    hWrite.write("Метод Рунге-Кутты\n")
    hWrite.write("  k  xk    yk             zk             dyk            dzk            yист           Ek\n");
    xm=[]
    ym=[]
    zm=[]
    while x<=Xend+h/10:
        dyk=Dy(h,f,g,x,y,z)
        dzk=Dz(h,f,g,x,y,z)
        yt=fans(x);
        e=abs(y-yt)
        zm.append(z);
        ym.append(y);
        xm.append(x);
        hWrite.write("{:3d}{:5.1f}{:15.10f}{:15.10f}{:15.10f}{:15.10f}{:15.10f}{:15.10f}\n".\
            format(k,x,y,z,dyk,dzk,yt,e));
        k+=1
        x+=h
        y+=dyk
        z+=dzk
    return xm,ym,zm
def metRRR(k,y1,y2,p):
    ym=[i for i in y1]
    hWrite.write("y=")
    for i in range(len(y1)):
        ym[i]=y2[i*k]+(y2[i*k]-y1[i])/(2**p-1)
        hWrite.write("{:15.10f}".format(ym[i]))
    hWrite.write("\n")
        
h=float(hRead.readline())
x=float(hRead.readline())
XK=float(hRead.readline())
y=float(hRead.readline())
z=float(hRead.readline())
xm1,ym1,zm1=metRK(h,f1,g1,x,y,z,fans1,XK);
xm2,ym2,zm2=euler_method(h,f1,g1,x,y,z,fans1,XK);
xm3,ym3,zm3=mod_euler_method(h,f1,g1,x,y,z,fans1,XK);
xm4,ym4,zm4=adams_method(h,f1,g1,fans1,xm1,ym1,zm1);
xm1_,ym1_,zm1_=metRK(h/2,f1,g1,x,y,z,fans1,XK);
xm2_,ym2_,zm2_=euler_method(h/2,f1,g1,x,y,z,fans1,XK);
xm3_,ym3_,zm3_=mod_euler_method(h/2,f1,g1,x,y,z,fans1,XK);
xm4_,ym4_,zm4_=adams_method(h/2,f1,g1,fans1,xm1_,ym1_,zm1_);
hWrite.write("улучшение методом Рунге-Ромберга-Ричардсона\n")
hWrite.write("x=")
for i in range(len(xm1)):
    hWrite.write("{:15.10f}".format(xm1[i]))
hWrite.write("\nправильный ответ\ny=")
for i in range(len(xm1)):
    hWrite.write("{:15.10f}".format(fans1(xm1[i])))
hWrite.write("\n")
hWrite.write("Метод Рунге-Кутта улучшеный\n")
metRRR(2,ym1,ym1_,2)
hWrite.write("Метод Эйлера улучшеный\n")
metRRR(2,ym2,ym2_,2)
hWrite.write("Метод Эйлера(мод) улучшеный\n")
metRRR(2,ym3,ym3_,2)
hWrite.write("метода Адама улучшеный\n")
metRRR(2,ym4,ym4_,2)
hRead.close()
hWrite.close()