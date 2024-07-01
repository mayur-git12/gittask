l=[1,2,3,4]
def my_map(fun,l):
    return [fun(item) for item in l]

print(my_map(lambda a:a**2, l ))