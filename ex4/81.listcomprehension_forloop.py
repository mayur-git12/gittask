#Ex1:
#square=[]
#for i in range(1,11):
#    square.append(i**2)
#print(square)

square2 = [i**2 for i in range(1,11)]
print(square2)

#Ex2:
#nagetive=[]
#for i in range(1,11):
#    nagetive.append(-i)
#print(nagetive)

nagetive2 = [-i for i in range(1,11)]
print(nagetive2)

#Ex3:
names=['abd','bha','urv']
#new_list=[]
#for name in names:
#    new_list.append(name[0])
#print(new_list)

new_list2=[name[0] for name in names]
print(new_list2)


