# append method:-(to insert data at last position)
things1=["abd","bha",20]
things1[0]="abdhish"
things1.append(10)
print(things1)

# insert method:-(to insert data at any position)
things2=["abd","bha",20]
things2.insert(2,10)
print(things2)

#using concatanation:-(in it we join the lists)
t3=['a','b',1]
t4=['b ','h',2]
t=t3+t4
print(t)

#using Extend method:-
t5=['a','b']
t6=['b ','h']
t5.extend(t6)
print(t5)