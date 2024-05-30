

def gay(lst,fnd, n=0,main=True):
    for i in range(len(lst)):
        if isinstance(lst[i],list):
            z=gay(lst[i],fnd, n, False)
            if not isinstance(z,list):
                return z
            n=z[0]
        else:
            if lst[i] == fnd:
                return n
            n+=1
    if main:
        return None
    return [n]



def gaysx(lst,word):
    def chx(lst):
        for x in lst:
            if isinstance(x,list):
                return True
        return False
    
    while chx(lst):
        lst2=[]
        for x in lst:
            if isinstance(x,list):
                lst2.extend(x)
            else:
                lst2.append(x)
        lst=lst2.copy()
    if word in lst:
        return lst.index(word)
    return None

word="asd"
lst=[[1,[4,[3,6],6],4], 2, [3, "asd", [5, [6, []],[1,2,3]]]]

print(gay(lst,word))
print(gaysx(lst,word))

a1=2
b1=2
k=3

def rasb(b,k,n=1):
    b=2*b**2+b
    n+=1
    if k !=n:
        b=rasb(b,k,n)
    return b

def rasa(a,b,k,n=1):
    if n==1:
        a=2*b+a
    else:
        b=rasb(b,n,1)
        a=2*b+a
    n+=1
    if k !=n:
        a=rasa(a,b,k,n)
    return a

print(rasb(b1,k))
print(rasa(a1,b1,k))

def rasbn(b,k):
    for i in range(k-1):
        b=2*b**2+b
    return b

def rasan(a,b,k):
    for i in range(k-1):
        a=2*b+a
        b=2*b**2+b
    return a
print(rasbn(b1,k))
print(rasan(a1,b1,k))