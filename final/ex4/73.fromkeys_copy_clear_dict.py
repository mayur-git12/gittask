#from keys:-
d1=dict.fromkeys(['name','age'],'unknown')   #we can use tuple insteed of list
print(d1)

d2=dict.fromkeys("abc",'unknown')
print(d2)

d3=dict.fromkeys(range(1,11),'unknown')
print(d3)

d4=dict.fromkeys(['name','age'],['unknown','unknown'])
print(d4)

#clear:-to clear dictionary
# d.clear()

#copy:-To copy data of dictionary to another dictionary
# d1=d.copy