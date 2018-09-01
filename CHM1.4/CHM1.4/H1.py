import math
def funLU(U,L,n):
    for i in range(n):
        for j in range(i,n):
            L[j][i]=U[j][i]/U[i][i]
    for k in range(1,n):
        for i in range(k-1,n):
            for j in range(i,n):
                L[j][i]=U[j][i]/U[i][i]
        for i in range(k,n):
            for j in range(k-1,n):
                U[i][j]=U[i][j]-L[i][k-1]*U[k-1][j]
def funLUP(U,L,P,n):
    e=0.00001
    y=0
    for k in range(0,n):
        for i in range(k,k+1):
            if abs(U[i][i])<e:
                y=0
                for j in range(i+1,n):
                    if abs(U[j][i])>e:
                        U[i],U[j]=U[j],U[i]
                        L[i],L[j]=L[j],L[i]
                        #for z in range(n):
                        #    L[z][i],L[z][j]=L[z][j],L[z][i]
                        #for z in range(n):
                        #    U[z][i],U[z][j]=U[z][j],U[z][i]
                        P[i],P[j]=P[j],P[i]
                        y=1
                        break
                if y==0:
                    print("ошибка")
                    SystemExit()
            for j in range(i,n):
                L[j][i]=U[j][i]/U[i][i]
        for i in range(k+1,n):
            for j in range(k,n):
                U[i][j]=U[i][j]-L[i][k]*U[k][j]
def multMat(L,U,n):
    LU =[[0 for i in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                LU[k][i]+=L[k][j]*U[j][i]
    return LU
def writeMat(U,hWrite):
    for i in U:
        hWrite.write("(")
        for j in i:
            hWrite.write(str(round(j, 4)))
            hWrite.write(" ")
        hWrite.write(")\n")
def printMat(U):
    for i in U:
        print("(",end="")
        for j in i:
            print(round(j, 4),end=" ")
        print(")")

def eqMat(U,n):
    A=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j]=U[i][j]
    return A
def opMatLU(U,n):
    a=1
    for i in range(n):
        a*=U[i][i]
    return a
def opMat(A,n):
    U=eqMat(A,n)
    L=[[0 for i in range(n)] for i in range(n)]
    funLU(U,L,n)
    return opMatLU(U,n)
def UMult(U,n,b):
    y=[0 for i in range(n)]
    for i in range(n):
        SUM=0
        for j in range(n-i,n):
            SUM-=y[j]*U[n-1-i][j]
        y[n-1-i]=(b[n-1-i]+SUM)/U[n-1-i][n-1-i]
    return y
def LMult(L,n,y):
    x=[0 for i in range(n)]
    for i in range(n):
        SUM=0
        for j in range(0,i):
            SUM-=x[j]*L[i][j]
        x[i]=(y[i]+SUM)/L[i][i]
    return x
def fiAns(U,L,n,b):
    return UMult(U,n,LMult(L,n,b))
def tranMat(A,n):
    for i in range(n):
        for j in range(n):
            if i>j:
                c=A[i][j]
                A[i][j]=A[j][i]
                A[j][i]=c
def multVM(v,m,n):
    y=[0 for i in range(n)] 
    for i in range(n):
        for j in range(n):
            y[i]+=v[j]*m[j][i]
    return y
def multMV(m,v,n):
    y=[0 for i in range(n)] 
    for i in range(n):
        for j in range(n):
            y[i]+=m[i][j]*v[j]
    return y
def metIt(A,S,n):
    e=0.00001
    x=[0 for i in range(n)]
    xN=[0 for i in range(n)]
    while True:
        y=True
        for i in range(n):
            xN[i]=S[i]/A[i][i]
            for j in range(n):
                if j!=i:
                    xN[i]-=x[j]*A[i][j]/A[i][i]
        for i in range(n):
            if abs(xN[i]-x[i])>e:
                y=False
            x[i]=xN[i]
        if y:
            return x
def metZeid(A,S,n):
    e=0.00001
    x=[0 for i in range(n)]
    while True:
        y=True
        for i in range(n):
            xN=S[i]/A[i][i]
            for j in range(n):
                if j!=i:
                    xN-=x[j]*A[i][j]/A[i][i]
            if abs(xN-x[i])>e:
                y=False
            x[i]=xN
        if y:
            return x
def writeV(V,hWrite):
    hWrite.write("(")
    for i in V:
        hWrite.write(str(round(i, 4)))
        hWrite.write(" ")
    hWrite.write(")\n")
def chekIak(A,n,e):
    zzz=0
    for i in range(n):
        for j in range(n):
            if i!=j:
                zzz+=A[i][j]**2;
    return zzz**0.5<e
def metIak(A,n,e):
    MU=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        MU[i][i]=1
    while True:
        x,y=0,1
        qf=0
        U =[[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            U[i][i]=1
        for i in range(n):
            for j in range(i+1,n):
                if abs(A[x][y])<abs(A[i][j]):
                    x,y=i,j
        if abs(A[x][x]-A[y][y])>e*0.01:
            qf=1/2*math.atan(2*A[x][y]/(A[x][x]-A[y][y]))
        else:
            qf=math.pi/4
        U[x][y]=-math.sin(qf)
        U[y][x]=math.sin(qf)
        U[y][y]=math.cos(qf)
        U[x][x]=math.cos(qf)
        MU=multMat(MU,U,n)#может здесь
        A=multMat(A,U,n)
        tranMat(U,n)
        A=multMat(U,A,n)
        if chekIak(A,n,e):
            return A,MU

