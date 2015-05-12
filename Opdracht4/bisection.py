# Bepalen van het nulpunt
def findRoot(f,a,b,epsilon):
    if f(a)>f(b):
        c=a
        a=b
        b=c

    m= (a+b)/2

    if abs(b-a)<=epsilon:
        return m
    
    if f(m)<=0:
        return findRoot(f,m,b,epsilon)
    else:
        return findRoot(f,a,m,epsilon)



def findAllRoots(f,a,b,epsilon):
    i = 0
    dx = (abs(a)+abs(b))/19
    nulpunten = []
    
    while (i<19):
        if ((f(a)<=0 and f(a+dx)>=0) or (f(a)>=0 and f(a+dx)<=0)):
            nulpunten.append(findRoot(f,a,a+dx,epsilon))
        a = a + dx
        i += 1

    return nulpunten
