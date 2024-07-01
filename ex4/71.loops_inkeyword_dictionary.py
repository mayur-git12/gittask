# key is in int/str form
user_info={
    'name':'abd',
    'age':20,
    'fav_movie':['tarzan','avengers'],
    'schools':['aradhna','exotica']
}

# check if key exist in dictionary
if 'name' in user_info:
    print('present')
else:
    print('not present')

# check if value in dictionary
if 20 in user_info.values():
    print('present')
else:
    print('not present')

# loops in dictionary:
for i in user_info:
    print(i)

# values in varials:
user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))

# print values using key in loop:
for i in user_info:
    print(user_info[i])

# items method:
user_items=user_info.items()
print(user_items)
print(type(user_items))
