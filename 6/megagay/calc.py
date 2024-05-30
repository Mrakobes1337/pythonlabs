from .inf import odezhdainf


def calc(all):
    all=norm(all)
    price=0
    for el in all:
        price+=el["price"]*el["amount"]
    return price

def norm(ton):
    ret=[]
    for el in ton.keys():
        if el in odezhdainf:
            to_ret={"price":odezhdainf[el][ton[f"{el}_type"]],"amount": ton[el]}
            ret.append(to_ret)
    return ret
