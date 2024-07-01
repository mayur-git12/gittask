d={'name':'abd','age':20}
#print(d['names']) (error)
print(d.get('name'))

if d.get('name'):
    print('present')
else:
    print('not present')

user={'name':'abd','age':20,'age':18}
#print(user.get('names','not found'))
print(user)