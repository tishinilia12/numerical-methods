hRead = open("F:\\test\\3.4\\14.txt", "r")
hWrite = open("F:\\test\\3.4\\ans14.txt","w")
n=int(hRead.readline())
X_=float(hRead.readline())
x=list(map(float, hRead.readline().split()))
y=list(map(float, hRead.readline().split()))
k=-1
t=False
for i in range(n):
    if X_>=x[i] and X_<x[i+1]:
        k=i
    if X_==x[i]:
        t=True
y2_1=(y[k]-y[k+1])/(x[k]-x[k+1])
y1_1=(y[k]-y[k-1])/(x[k]-x[k-1])
y_2=2*(y2_1-y1_1)/(x[k+1]-x[k-1])
if t:
    hWrite.write(f'f\'({X_})= {(y1_1+y2_1)/2}\n')
else:
    hWrite.write(f'f\'({X_})= {y2_1}\n')
hWrite.write(f'f\'\'({X_})= {y_2}\n')
hRead.close()
hWrite.close()

