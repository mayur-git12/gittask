def mul_num(*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply

num=[2,2,3,4]
print(mul_num(*num))   #Unpack