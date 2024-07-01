from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args, **kwargs)
            print("invalid arg")
        return wrapper
    return decorator
@only_data_type_allow(str)
def str_join(*args):
    string=''
    for i in args:
        string += i
    return string

print(str_join('abdhish','bhavsar',8))

