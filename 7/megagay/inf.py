from abc import abstractclassmethod, ABC
odezhdainf={
    "tkan":{"name":"Ткань","types":{"rich":100,"normal":50}},
    "pugov":{"name":"Пуговицы","types":{"rich":20,"normal":10}},
    "ukrash":{"name":"Украшения","types":{"rich":70,"normal":35}},
    "zamok":{"name":"Замки","types":{"rich":25,"normal":15}},
}

class Odezhda(ABC):
    
    tkan=None
    tkan_type=None
    pugov=None
    pugov_type=None
    zamok=None
    zamok_type=None
    ukrash=None
    ukrash_type=None
    @abstractclassmethod   
    def __init__(self):
        super().__init__()
    
    
    def calc(self):
        all=self.norm()
        price=0
        for el in all:
            price+=el["price"]*el["amount"]
        return price
    
    def norm(self):
        ton=self.__dict__
        ret=[]
        for el in ton:
            if el in odezhdainf:
                to_ret={"price":odezhdainf[el]["types"][ton[f"{el}_type"]],"amount": ton[el]}
                ret.append(to_ret)
        return ret


class Pid(Odezhda):
    def __init__(self,tkan=10,tkan_type="rich",pugov=8,pugov_type="normal"):
        self.tkan=tkan
        self.tkan_type=tkan_type
        self.pugov=pugov
        self.pugov_type=pugov_type
        self.gay=1
    def __del__(self):
        print("О нет, ты съел пиджак")
        
    @property
    def gay(self):
        return self._gay
    
    @gay.setter
    def gay(self,new):
        self._gay=new
    

class Bruk(Odezhda):
    def __init__(self,tkan=8,tkan_type="normal",zamok=1,zamok_type="normal"):
        self.tkan=tkan
        self.tkan_type=tkan_type
        self.zamok=zamok
        self.zamok_type=zamok_type
        self.gay=1
        
    def __del__(self):
        print("О нет, ты съел брюки")
    
    @property
    def gay(self):
        return self._gay
    
    @gay.setter
    def gay(self,new):
        self._gay=new
    
        
        
        
class Troika(Odezhda):
    def __init__(self,tkan=8,tkan_type="rich",pugov=2,pugov_type="rich",zamok=1,zamok_type="rich",ukrash=10,ukrash_type="rich"):
        self.tkan=tkan
        self.tkan_type=tkan_type
        self.pugov=pugov
        self.pugov_type=pugov_type
        self.zamok=zamok
        self.zamok_type=zamok_type
        self.ukrash=ukrash
        self.ukrash_type=ukrash_type
        self.gay=1
    def __del__(self):
        print("О нет, ты съел костюм")
        
        
    @property
    def gay(self):
        return self._gay
    
    @gay.setter
    def gay(self,new):
        self._gay=new
    
    
    
classes={"Пиджак":Pid,
         "Брюки":Bruk,
         "Костюм-тройка":Troika}