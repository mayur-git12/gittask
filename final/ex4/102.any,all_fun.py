#Ex:1:-
num1=[1,2,3,4,5]
print(any([num%2==0 for num in num1]))

#Ex2:-
def my_sum(*args):
    if all([(type(arg)==int or type(arg)==float)for arg in args]):
        total=0
        for num in args:
            total=num+total
        return total
    else:
        return "wrong input"
    
print(my_sum(1,2,5.3,4.1,'abd'))