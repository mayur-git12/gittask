class phone: #parant/base
    def __init__(self,name,modle,price):
        self.name=name
        self.modle=modle
        self.price=max(price,0)

    def full_name(self):
        return f"{self.name} {self.modle}"

   

class smart_phone(phone): #derived/child
    def __init__(self,name,modle,price,ram,rom,os):
        #phone. __init__(self,name,modle,price) #uncomman way
        super().__init__(name,modle,price)

        self.ram=ram
        self.rom=rom
        self.os=os
        

p1=phone('oppo','f3',19000)
print(p1.full_name())
sp1=smart_phone('mi','a5','25000','4','64','10')
print(sp1.full_name())
