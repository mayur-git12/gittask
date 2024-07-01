class A:
    def class_A(self):
        return 'A'
    def hello(self):
        return 'hello A'

class B:
    def class_B(self):
        return 'B'
    def hello(self):
        return 'hello B'

class c(A,B):
    pass

c1=c()
print(c1.class_A())
print(c1.class_B())
print(c1.hello())