def decorator_fun(any_fun):
    def wrapper_fun(*args, **kwargs):
        print("this is awesome")
        return any_fun(*args, **kwargs)
    return wrapper_fun
    
@decorator_fun
def fun(a):
    print(f"this is fun with arg {a}")
fun(4)

@decorator_fun
def add(a,b):
    return a+b
print(add(2,4))