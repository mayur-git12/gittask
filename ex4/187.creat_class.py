class Person:
    def __init__(self, first_name, last_name, age):   #self=instance, others are attributes in function
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.name=first_name+last_name+age
        
p1=Person('abd', ' bha', ' 21')
p2=Person('rishi',' nuwal',' 22')
print(p1.name)