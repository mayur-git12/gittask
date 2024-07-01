#Decoreters: Enhance the functionality of other functions
# @:-syntactic sugar (used for decoraters)

def decorator_fun(any_fun):
    def wrapper_fun():
        print("this is awesome")
        any_fun()
    return wrapper_fun
    
def fun1():
    print("this is fun 1")

@decorator_fun   #Shortcut to enhance functionality
def fun2():
    print("this is fun 2")
fun2()

var = decorator_fun(fun1)
var()