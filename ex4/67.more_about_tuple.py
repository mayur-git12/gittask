# Looping with tuple:-
t1=('1','2','3','4.0')
for i in t1:
    print(i)
i=0
while i<len(t1) :
    print(t1[i])
    i=i+1
   
# tuple with 1 element:-
n1=(1)
n2=(1,)
w1=('word')
w2=('word',)
print(type(n1))
print(type(n2))
print(type(w1))
print(type(w2))

#tuple witout parantheses:-
school='aradhna','exotica','gitangli'
print(type(school))

#tuple unpacking:-
school1,school2,school3=(school)
print(school2)

#list inside tuple:-
city=('delhy',['gandhinagar','talod'])
city[1].pop()
print(city)