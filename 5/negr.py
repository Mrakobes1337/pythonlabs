import os

def check(ras,path=os.getcwd(),katl=False,ren="test"):
    def filtr(name):
        if name.split(".")[-1].lower() == ras.lower():
            return True
        else:
            return False
    def walker(path,n=-1):
        walk=next(os.walk(path))
        files=(file for file in walk[2])
        files=list(filter(filtr,files))
        ftext="\n".join(list(filter(filtr,files)))
        kat="/".join(path.split("/")[n:])
        if files:
            print(f'Каталог {kat}:\n{ftext}\n\n')
        for i,file in enumerate(sorted(files),start=1):
            os.rename(f"{path}/{file}",f"{path}/{ren}{i}.{ras}")
        for w in walk[1]:
            walker(f"{walk[0]}/{w}",n-1)
    if katl:
        walker(path)
    else:
        walk=next(os.walk(path))
        files=(file for file in walk[2])
        files=list(filter(filtr,files))
        print("\n".join(files))
        for i,file in enumerate(sorted(files),start=1):
            os.rename(f"{path}/{file}",f"{path}/{ren}{i}.{ras}")
        
    
check("py",os.getcwd()+"/5",True,"gay") 
