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

class flagship_phone(smart_phone):
    def __init__(self,name,modle,price,ram,rom,os,camera):
        super(). __init__(name,modle,price,ram,rom,os)

        self.camera=camera

fp1=flagship_phone('oppo','f3',19000,'4','64',6.0,'13mp')
print(fp1.camera)

# print(help(smart_phone))  # Method Resolution order