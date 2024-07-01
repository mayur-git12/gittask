class circle:
    count_instance=0
    pi=3.14     #class variable
    def __init__(self,radius):
        circle.count_instance+=1
        self.radius=radius

    def circumference(self):
        return 2*circle.pi*self.radius
   

c1=circle(4)
c2=circle(5)
print(c1.circumference())
print(circle.count_instance)

 

