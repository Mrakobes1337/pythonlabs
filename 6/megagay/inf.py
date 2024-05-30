
odezhdainf={
    "tkan":{"rich":100,"normal":50},
    "pugov":{"rich":20,"normal":10},
    "ukrash":{"rich":70,"normal":35},
    "zamok":{"rich":25,"normal":15},
}

class Odezhda:
    tkan=None
    tkan_type=None
    pugov=None
    pugov_type=None
    zamok=None
    zamok_type=None
    ukrash=None
    ukrash_type=None

class Pid(Odezhda):
    def __init__(self,tkan=10,tkan_type="rich",pugov=8,pugov_type="normal"):
        self.tkan=tkan
        self.tkan_type=tkan_type
        self.pugov=pugov
        self.pugov_type=pugov_type
        

class Bruk(Odezhda):
    def __init__(self,tkan=8,tkan_type="normal",zamok=1,zamok_type="normal"):
        self.tkan=tkan
        self.tkan_type=tkan_type
        self.zamok=zamok
        self.zamok_type=zamok_type
     
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
    
classes={"Пиджак":Pid,
         "Брюки":Bruk,
         "Костюм-тройка":Troika}