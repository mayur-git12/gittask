def mul_num(num,*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply
print(mul_num(2,3,4,5))