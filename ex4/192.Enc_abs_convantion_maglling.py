#encapulation:-use many methods in single class
class laptop:
    def __init__(self,brand,model,price,discount_per):
        self.brand_name=brand
        self.model_num=model
        self.price=price
        self.discount_per=discount_per

    def amount_after_discount(self):
        #x=int(input('enter discount percentage:'))
        return f"{self.price-self.price*(self.discount_per/100)}"

    def send_msg(self):
        pass #twillio

#_name:-convantion of private name
#__name__:-dunder/magic method

l1=laptop('lenovo','A1',50000,20)
l=[1,3,5,4,2]
l.sort()  #abstraction:-To minimize complexity 
print(l)