 


def negr_pobolbshe(br):
    elms=[]
    def negr_pomenbshe(el):
        if el==br:
            ret=elms.copy()
            elms.clear()
            return ret
        elms.append(el)
    return negr_pomenbshe
bobik=negr_pobolbshe(0)
bobik(1)
bobik(2)
bobik(4)
bobik(3)
bobik(5)
bobik(6)
print(bobik(0))
bobik(11)
bobik(2)
bobik(4)
bobik(3)
bobik(5)
bobik(8)
print(bobik(0))





def validate(x,y):
    def dec(fun):
        def checks(v1,v2):
            if x(v1) and y(v2):
                fun(v1,v2)
            else:
                raise Exception("Поражение")
        return checks
    return dec

@validate(lambda x: x > 0, lambda y: isinstance(y, str))
def my_function(x, y):
    print("Победа")
    
my_function(1,"негр")
my_function(1,5)