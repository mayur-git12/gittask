#generate list with range function:-
num=list(range(1,11))
print(num)

#Find removed element using pop:-
p1=['1','5','3','4']
print(p1.pop(1))

# Find position of perticular element using index method:-
p2=['1','5','3','4','2','1']
print(p2.index('5'))

#pass list to function:-
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(num))
        