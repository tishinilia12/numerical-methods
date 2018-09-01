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
    j1=0
    y=0
    for k in range(0,n):
        for i in range(k,k+1):
            e=abs(U[i][i])
            j1=i;
            for j in range(i+1,n):
                if abs(U[j][i])>e:
                    y=1
                    e=abs(U[j][i])
                    j1=j
            if y==0:
                print("ошибка")
            U[i],U[j1]=U[j1],U[i]
            L[i],L[j1]=L[j1],L[i]
            P[i],P[j1]=P[j1],P[i]
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
def chekIt(m,n):
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if i!=j:
                tmp+=m[i][j]/m[i][i]
        ans=max(tmp,ans)
    return ans