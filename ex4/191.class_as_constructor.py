class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
    
    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

   
        
p1=Person('abd', ' bha', 21)
p2=Person('rishi',' nuwal',22)
p3=Person.from_string('dhaval,thakor,22')
print(p3.full_name())
