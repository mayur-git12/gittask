class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_21(self):
        return self.age>21
        
p1=Person('abd', ' bha', 21)
p2=Person('rishi',' nuwal',22)
print(p1.full_name())
print(Person.full_name(p2))

print(p1.is_above_21())