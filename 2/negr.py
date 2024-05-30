 
import itertools
def gay(z):
    def gayz(x):
        return "И" not in x
    return len(list(itertools.filterfalse(gayz,list(itertools.combinations_with_replacement(z,5)))))

print(gay("ИВАН"))


def gay2(x):    
    return oct(x)[2:].count("0")

print(gay2(7*512**120-6*64**100+8**210-255))


def gay3(x1,x2):

    maxmax=0
    mini=0
    for i in range(x1, x2+1):
        n=0
        for j in range(1,i+1):
            if i%j==0:
                n+=1
        if maxmax<n:
            maxmax=n
            mini=i
    return [maxmax,mini]

print(gay3(1,48))