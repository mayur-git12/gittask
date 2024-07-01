s='i    am   abd'
new=s.split(' ')
print(new)

l2=[]
for i in new:
    if i:
        l2.append(i)
    else:
        pass
print(l2)
print(len(l2))