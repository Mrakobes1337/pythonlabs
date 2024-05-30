


lsts=[1, 2, [3, "spam", [5, [6, []]]]]
s="spam"
def gaysx(word,lst1):
    def chx(lst):
        for x in lst:
            if isinstance(x,list):
                return True
        return False
    def nig(lst):
        lst2=[]
        for x in lst:
            if isinstance(x,list):
                lst2.extend(x)
            else:
                lst2.append(x)
        return lst2

    while chx(lst1):
        lst1=nig(lst1)
    if word in lst1:
        return lst1.index(word)
    return None


#print(gaysx(s,lsts))
n=1
a1=2
b1=2
k=3

#def rasb(b,n,k):
#    bk=b
#    for i in range(n+2,k+1):
#        bk=2*bk**2
def rasb(b,n,k):
    b=2*b**2+b
    n+=1
    if k !=n:
        b=rasb(b,n,k)
    return b
def rasa(a,b,n,k):
    if n==1:
        a=2*b+a
    else:
        b=rasb(b,1,n)
        a=2*b+a
    n+=1
    if k !=n:
        a=rasa(a,b,n,k)
    return a
print(rasb(b1,n,k))
print(rasa(a1,b1,n,k))

b=b1

a=a1
b=b1

print(a)