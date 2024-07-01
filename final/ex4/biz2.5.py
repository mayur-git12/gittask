# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the
# value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106


a=int(input('enter num:'))
b=a*11
c=a*111
d=a*1111
print(f'{a+b+c+d}')
