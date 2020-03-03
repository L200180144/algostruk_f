from math import sqrt as s
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    
    D=(b**2)-(4*a*c)
    if D>0:
        x1=(-b+s(D))/(2*a)
        x2=(-b-s(D))/(2*a)
        hasil=(x1,x2)
        print (hasil)
    else:
        print ("Determinan negatif. Persamaan tidak mempunyai akar real")

