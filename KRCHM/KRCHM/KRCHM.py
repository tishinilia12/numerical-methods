hRead = open("F:\\test\\KR\\test3.txt", "r")
import matplotlib as mpl 
import matplotlib.pyplot as plt
import math
def h(i,x):
    if i==-1:
        return h(i+1,x)
    if i+1==len(x):
        print("bad")
    return x[i+1]-x[i];
def x1_2(i,x):
    return (x[i]+x[i+1])/2
def dL2(y,i,B,x):
    #return y[i+1]*math.sinh(B*(h(i+1,x)+h(i,x)))/math.sinh(B*h(i,x))#+y[i+2]
    return (y[i]*math.sinh(B*h(i+1,x))/math.sinh(B*h(i,x))-\
y[i+1]*math.sinh(B*(h(i+1,x)+h(i,x)))/math.sinh(B*h(i,x)))+y[i+2]
def a_j(j,x,y,B):
    return -(math.sinh(B*h(j-1,x)/4))*dL2(y,j-1,B,x)\
        /(2*math.sinh(B*h(j,x)/4)*math.sinh(B*(h(j,x)+h(j-1,x))/4)*math.sinh(B*h(j,x)))
def b_j(j,x,y,B):
    return (1/math.sinh(B*h(j,x)/2))*\
        ((y[j+1]+y[j])/2-y[j]*math.cosh(B*h(j,x)/2)-\
        math.sinh(B*h(j-1,x)/4)*(math.cosh(B*h(j,x)/2)-1)*dL2(y,j-1,B,x)/\
        (2*math.sinh(B*h(j,x)/4)*math.sinh(B*(h(j,x)+h(j-1,x))/4)*math.sinh(B*h(j,x))))
def c_j(j,x,y,B):#*math.cosh(B*h(j,x)/2)\
    return y[j]+(math.sinh(B*h(j-1,x)/4))*dL2(y,j-1,B,x)\
        /(2*math.sinh(B*h(j,x)/4)*math.sinh(B*(h(j,x)+h(j-1,x))/4)*math.sinh(B*h(j,x)))
def d_j(j,x,y,B):
    return (math.sinh(B*h(j-1,x)/4))*dL2(y,j-1,B,x)\
        /(2*math.sinh(B*h(j,x)/4)*math.sinh(B*(h(j,x)+h(j-1,x))/4)*math.sinh(B*h(j,x))\
        *(math.cosh(B*h(j,x)/2)-1))+\
        math.sinh(B*h(j-1,x)/4)*(math.cosh(B*h(j,x)/2)-1)*dL2(y,j-1,B,x)/\
        (2*math.sinh(B*h(j,x)/4)*math.sinh(B*(h(j,x)+h(j-1,x))/4)*math.sinh(B*h(j,x)/2)\
        *(math.cosh(B*h(j,x)/2)-1))-\
        (math.sinh(B*h(j-1,x)/4))*dL2(y,j-1,B,x)*math.cosh(B*h(j,x))\
        /(2*math.sinh(B*h(j,x)/4)*math.sinh(B*(h(j,x)+h(j-1,x))/4)*math.sinh(B*h(j,x))\
        *(math.cosh(B*h(j,x)/2)-1))\
        -y[j]*math.cosh(B*h(j,x))/(math.cosh(B*h(j,x)/2)-1)\
        -(y[j+1]+y[j])*math.sinh(B*h(j,x))/2/math.sinh(B*h(j,x)/2)/(math.cosh(B*h(j,x)/2)-1)\
        +(y[j]*math.sinh(B*h(j,x))*math.cosh(B*h(j,x)/2))/math.sinh(B*h(j,x)/2)/(math.cosh(B*h(j,x)/2)-1)\
        +y[j+1]/(math.cosh(B*h(j,x)/2)-1)

'''(math.sinh(B*h(j-1,x)/4))*dL2(y,j-1,B,x)/(2*math.sinh(B*h(j,x)/4)*math.sinh(B*(h(j,x)+h(j-1,x)/4)\
        *math.sinh(B*h(j-1,x))))-(math.sinh(B*h(j-1,x)/4))*dL2(y,j-1,B,x)\
        /(2*math.sinh(B*h(j,x)/4)*math.sinh(B*(h(j,x)+h(j-1,x)/4)*math.sinh(B*h(j,x))))'''
def t(x):
    if x<0:
        x=0;
    return x
def S(x,ym,x_t,B):
    y=[i for i in ym]
    y.append(y[-1])
    i=0
    while not(x[i+1]>=x_t and x_t>x[i]):
        i+=1
    return a_j(i,x,y,B)+b_j(i,x,y,B)*(math.sinh(B*(x_t-x[i])))+c_j(i,x,y,B)*math.cosh(B*(x_t-x[i]))+\
        d_j(i,x,y,B)*(math.cosh(B*(t(x_t-x1_2(i,x))))-1)


x=list(map(float, hRead.readline().split()))
y=list(map(float, hRead.readline().split()))
B=float(hRead.readline())
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.axis([x[0], x[-1], min(y)-0.5, max(y)+0.5])

plt.title('exp spline')
plt.xlabel('x')
plt.ylabel('F(x)')
x_t=x[0]+0.00001
xs = []
s_vals = []
while x_t < x[-1]:
    s_vals += [ S(x,y,x_t,B) ]
    xs += [x_t] 
    x_t += 0.007
plt.plot(xs, s_vals, color = 'blue', linestyle = 'solid',label = 'exp SP1')
plt.plot(x, y, color = 'red', linestyle = 'solid',label = 'line')
plt.legend(loc = 'upper right')
fig.savefig('F:\\test\\KR\\expSP3.png')
hRead.close()
