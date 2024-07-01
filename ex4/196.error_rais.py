def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError("you enterd wrong datatype")

print(add('2','3'))