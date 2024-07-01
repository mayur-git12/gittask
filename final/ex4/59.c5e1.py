num=[1,2,3,4,5]
def square_list(l):
    square=[]
    for i in num:
        square.append(i**2)
    return square
print(square_list(num))
