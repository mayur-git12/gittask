
from functools import wraps
def decorator_fun(any_fun):
    @wraps (any_fun)
    def wrapper_fun(*args, **kwargs):
        '''this is wrapper fun'''
        print("this is awesome")
        return any_fun(*args, **kwargs)
    return wrapper_fun

def add(a,b):
    '''this is add fun'''
    return a+b
print(add.__doc__)
print(add.__name__)