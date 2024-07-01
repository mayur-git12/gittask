word='i am abd'
new=word.split(' ')
mylist=[]

for i in new:
    mylist.append(i[-1::-1])
f_sen=' '.join(mylist)
print(f_sen)
