# set is DataType
# Unorderd collection of Unique Items
#Cant Store Dict,List,Tupples in SET.
s={1,2,3,4,2,3}  
print(s)

#remove duplicate elements in list:
l=[1,2,3,2,3]
s2=list(set(l))
print(s2)

#add:
s3={1,2,3,4}
s3.add(5)
print(s3)

#Remove:
s4={1,2,3,4}
s4.remove(2)
               #s4.remove(6) {Error Because 6 not in set}
print(s4)

#Discard:(dont show error if element not in set during discarding. )
s5={1,2,3,4}
s5.discard(6)
print(s5)

#clear:
s6={1,2,3}
s6.clear()
print(s6)

#copy:
s7=s.copy()
print(s7)