hRead = open("F:\\test\\3.5\\14.txt", "r")
hWrite = open("F:\\test\\3.5\\ans14.txt","w")
def f2(x):
    return 1/(x**4+16)
def f1(x):
    return x/((3*x+4)**2)
def metangl(h,f,X0,XK,hWrite):
    hWrite.write(f'метод прямоугольников при h={h}\n')
    ans=0
    s=X0
    while s<XK:
        ans+=f((2*s+h)/2)*h
        s+=h
        hWrite.write(f'x={round(s,5)},y={round(f(s),5)},F={round(ans,5)}\n')
    hWrite.write(f'\n\n')
    return ans
def mettrp(h,f,X0,XK,hWrite):
    hWrite.write(f'метод трапеций при h={h}\n')
    ans=0
    s=X0
    while s<XK+h*0.001:
        if s==X0 or s+h*0.001>XK:
            ans+=f(s)/2*h
        else:
            ans+=f(s)*h
        hWrite.write(f'x={round(s,5)},y={round(f(s),5)},F={round(ans,5)}\n')
        s+=h
    hWrite.write(f'\n\n')
    return ans
def metsim(h,f,X0,XK,hWrite):
    hWrite.write(f'метод Симпсона при h={h}\n')
    ans=0
    s=X0
    while s<XK+h*0.001:
        if s==X0 or s+h*.001>XK:
            ans+=f(s)*h/3
            hWrite.write(f'x={round(s,5)},y={round(f(s),5)},F={round(ans,5)}\n')
            s+=h
        elif s+h*1.001>XK:
            ans+=(4*f(s)+f(s+h))*h/3
            hWrite.write(f'x={round(s,5)},y={round(f(s),5)},F={round(ans,5)}\n')
            s+=2*h
        else:
            ans+=(4*f(s)+2*f(s+h))*h/3
            hWrite.write(f'x={round(s,5)},y={round(f(s),5)},F[{round(X0,5)},{round(s,5)}]={round(ans,5)}\n')
            s+=2*h
    hWrite.write(f'\n\n')
    return ans
def metRRR(x,y,k,p):
    return y+(y-x)/((k**p)-1)
X0=float(hRead.readline())
XK=float(hRead.readline())
h1=float(hRead.readline())
h2=float(hRead.readline())
resh=float(hRead.readline())
x1=metangl(h1,f2,X0,XK,hWrite);
x2=mettrp(h1,f2,X0,XK,hWrite);
x3=metsim(h1,f2,X0,XK,hWrite);
y1=metangl(h2,f2,X0,XK,hWrite);
y2=mettrp(h2,f2,X0,XK,hWrite);
y3=metsim(h2,f2,X0,XK,hWrite);
hWrite.write(f'ответ {resh}\n')
hWrite.write(f'метод прямоугольников {round(metRRR(x1,y1,h1/h2,2),5)},абсолютная погрешность {abs(round(metRRR(x1,y1,h1/h2,2)-resh,5))}\n')
hWrite.write(f'метод трапеций {round(metRRR(x2,y2,h1/h2,2),5)},абсолютная погрешность {abs(round(metRRR(x2,y2,h1/h2,2)-resh,5))}\n')
hWrite.write(f'метод Симпсона {round(metRRR(x3,y3,h1/h2,2),5)},абсолютная погрешность {abs(round(metRRR(x3,y3,h1/h2,2)-resh,5))}\n')
hRead.close()
hWrite.close()
