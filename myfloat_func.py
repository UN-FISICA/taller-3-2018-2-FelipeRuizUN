#!/usr/bin/python
# -*- coding: UTF-8 -*- 
def tup (a):
    if a<0:
       c=-1*a
    else:
        c=a
    if type(a) is int:
        c1=list(map(int, str(c)))
        c2=[0]
    if type(a) is float:
        c1=list(map(int, str(int(c))))
        c2=list(map(int, str(c).split('.')[1]))
    if a>=0:
        c1.insert(0,'+')
    else:
        c1.insert(0,'-')
    return(c1,c2)
def imp(a):#convierte una lista de numeros en un entero
    a1=''
    for i in range(len(a)): 
        a1+=str(a[i])
    return int(a1)
def res(a,b):
    s=([],[])    
    for i in range(len(a[1]),1,-1):
        if a[1][i-1]<b[1][i-1]:
            a[1][i-1]+=10
            a[1][i-2]-=1
        s[1].insert(0,a[1][i-1]-b[1][i-1])
    if a[1][0]<b[1][0]:
        a[1][0]+=10
        a[0][-1]-=1
    for i in range(len(a[0]),1,-1):
        if a[0][i-1]<b[0][i-1]:
            a[0][i-1]+=10
            a[0][i-2]-=1
        s[0].insert(0,a[0][i-1]-b[0][i-1])
    s[0].insert(0,a[0][0])
    for j in range(0,len(a[0])-2):
        if s[0][1]==0:
            s[0].pop(1)
    return s
       	
def imprimir(a):
    b1=''
    b2=''
    for i in range(len(a[0])): 
        b1+=str(a[0][i])
    for j in range(len(a[1])):
        b2+=str(a[1][j])
    return (b1+","+b2)
def ceros(a,b):
    if len(a[1])>len(b[1]):
        for i in range (len(a[1])-len(b[1])):
            b[1].append(0)
    elif len(b[1])>len(a[1]):
        for i in range (len(b[1])-len(a[1])):
            a[1].append(0)
    if len(a[0])>len(b[0]):
        for i in range (len(a[0])-len(b[0])):
            b[0].insert(1,0)
    elif len(b[0])>len(a[0]):
        for i in range (len(b[0])-len(a[0])):
            a[0].insert(1,0)
def noceros(a):
    for j in range(len(a)):
        if a[0]==0:
            a.pop(0)    
    return(a)
def normal(a):
    for j in range(len(a[0])-2):
        if a[0][1]==0:
            a[0].pop(1)
    for j in range(len(a[1]),1,-1):
        if a[1][-1]==0:
            a[1].pop(-1)
    return(a)	 	
def suma(a,b):
    c1=[]
    c2=[]
    S=([],[])
    ceros(a,b)
    if a[0][0]==b[0][0]:
        S[1].append((a[1][-1]+b[1][-1])%10)
        for i in range(len(a[1])-1,0,-1):
            S[1].insert(0,(a[1][i-1]+b[1][i-1]+(a[1][i]+b[1][i])//10)%10)
			
        S[0].append((a[0][-1]+b[0][-1]+(a[1][0]+b[1][0])//10)%10)
		
        for i in range(len(a[0])-1,1,-1):
            S[0].insert(0,(a[0][i-1]+b[0][i-1]+(a[0][i]+b[0][i])//10)%10)
        S[0].insert(0,a[0][0])
    else:
        if imp(a[0][1::])>imp(b[0][1::]):
            c1=a[0][:]
            c2=a[1][:]
        elif imp(a[0][1::])<imp(b[0][1::]):
            c1=b[0][:]
            c2=b[1][:]
        c=(c1,c2)        
        if (c!=a)and(c!=b):
            if imp(a[1])>imp(b[1]):
                c1=a[0][:]
                c2=a[1][:]
            elif imp([1])<imp(b[1]):
                c1=b[0][:]
                c2=b[1][:]
            else:
                c=a
        c=(c1,c2)
        if c==a:
            S=res(c,b)
        elif c==b:
            S=res(c,a)
        
    return S
   
def resta(a,b):
    c1=b[0][:]
    c2=b[1][:]
    c=(c1,c2)
    if c[0][0]=='+':
        c[0][0]='-'
    elif c[0][0]=='-':
        c[0][0]='+'
    return suma(a,c)
def multiplicacion(a,b):
    c=0
    M=(['+',0],[0])
    m=(['+'],[])
    a1=a[0][:]    
    a1.pop(0)
    a1.extend(a[1])
    b1=b[0][:]
    b1.pop(0)
    b1.extend(b[1])
    for j in range(len(a1),0,-1):
        m[0].append(a1[j-1]*b1[-1]%10)        
        for i in range(len(b1)-1,0,-1):
            m[0].insert(1,(a1[j-1]*b1[i-1]+(a1[j-1]*b1[i])//10)%10)
        for k in range(c):
            m[0].append(0)
        if a1[j-1]*b1[0]>=10:
            m[0].insert(1, (a1[j-1]*b1[0])//10)
        M=suma(M,m)       
        c+=1
        m=(['+'],[])
    
    for n in range(len(b[1])+len(a[1]),0,-1):
        M[1].insert(0,M[0][-1])
        M[0].pop(-1)
    if a[0][0]==b[0][0]:
        M[0][0]='+'
    else:
        M[0][0]='-'
    return normal(M)
def division(a,b,n=100):
    c=max(len(b[1]),len(a[1]))
    for i in range(c-len(a[1])):
        a[1].append(0)
    for j in range(c-len(b[1])):
        b[1].append(0)
    a1=a[0][:]    
    a1.pop(0)
    a1.extend(a[1])
    b1=b[0][:]
    b1.pop(0)
    b1.extend(b[1])
    noceros(a1)
    noceros(b1)
    a1=imp(a1)
    b1=imp(b1)
    d1= list(map(int, str(a1//b1)))
    d2=[]
    res=a1%b1    
    for k in range(n):
        div=res*10
        prod=div//b1*b1
        d2.append(div//b1)
        res=div-prod
    D=(d1,d2)
    if a[0][0]==b[0][0]:
        D[0].insert(0,'+')
    else:
         D[0].insert(0,'-')
                
    return normal(D)     
def comparacion(a,b):
    if normal(a)==normal(b):
        return True
    else:
        return False
