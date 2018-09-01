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
def writeMatCom(U,hWrite):
    for i in U:
        hWrite.write("(")
        for j in i:
            x=complex(j)
            x1=x.real
            x2=x.imag
            hWrite.write(str(round(x1, 4)))
            hWrite.write(" ")
            hWrite.write(str(round(x2, 4)))
            hWrite.write("j ")
        hWrite.write(")\n")
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
            print(j,end=" ")
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
def chekQR(A,n,e,i):
    zzz=0
    for j in range(i+1,n):
         zzz+=A[j][i]**2;
    return zzz**0.5<e
def chekQRP(A,n,e,i):
    zzz=0
    for j in range(i+2,n):
        zzz+=A[j][i]**2;
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
def matMis(A,B,n):
    H=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            H[i][j]=A[i][j]-B[i][j]
    return H
def bildV(A,k,n):
    V =[0 for i in range(n)]
    s=0
    for i in range(k,n):
        s+=A[i][k]**2
        V[i]=A[i][k]
    V[k]+=s**0.5*A[k][k]/abs(A[k][k])
    return V
def multVTV(VT,V,n):
    sum=0
    for i in range(n):
        sum+=VT[i]*V[i]
    return sum
def multVVT(V,VT,n):
    H=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            H[i][j]+=V[i]*VT[j]
    return H
def multMatNum(A,k,n):
    H=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
             H[i][j]=A[i][j]*k
    return H
def bildH(A,k,n):
    H=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        H[i][i]=1
    V=bildV(A,k,n)
    H=matMis(H,multMatNum(multVVT(V,V,n),2/multVTV(V,V,n),n),n)
    return H
def bildQ(A,n):
    Q=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        Q[i][i]=1
    for i in range(n-1):
        H=bildH(A,i,n)
        A=multMat(H,A,n)
        Q=multMat(Q,H,n)
    return Q