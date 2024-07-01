
class laptop:
    def __init__(self,brand,model,price,discount_per):
        self.brand_name=brand
        self.model_num=model
        self.price=price
        self.discount_per=discount_per

    def amount_after_discount(self):
        #x=int(input('enter discount percentage:'))
        return f"{self.price-self.price*(self.discount_per/100)}"

l1=laptop('lenovo','A1',50000,20)
l2=laptop('acer','A5',42000,10)
l3=laptop('hp','A2',48000,5)
print(l1.brand_name)
print(l2.amount_after_discount())
print(l3.amount_after_discount())
