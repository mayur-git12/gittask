# I have two lists :
# lst_a = [1,2,3,4,9,,5,6]
# lst_b = [7,8,4,9,10,1]
# a) find the same elements in the list.
# b) make a Union of these two lists into a third list.
# c) Make intersection of these two lists into a third list.

a=[1,2,3,4,9,5,6]
b=[7,8,4,9,10,1]



s1=set(a)
s2=set(b)

u=s1|s2
print(list(u))

I=s1&s2           # answer of a
print(list(I))

