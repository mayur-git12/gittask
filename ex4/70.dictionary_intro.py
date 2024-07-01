# Q:why we use dictionaries?
# A: limitations of list,lists are not enough to represent real data.

# Q:What are dictionaries?
# A: Unorderd collection of data in {key:value} pair

#Dictionary can store any type of data(i.e num,str,list,dictionary)

#Methods to creat dictionary:-
#M1:
user={'name':'abdhish','age':20}
print(user)

#M2:
user2 = dict(name='abdhish',age=20)
print(user2)

# Access data in dictionary:-
print(user['name'])

#How to add data into dictionary:-
user_info={}
user_info['name']='abd'
print(user_info)