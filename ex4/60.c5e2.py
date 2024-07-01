l=[1,2,3]
def reversed_list(l):
    r_list=[]
    for i in range(len(l)):
        poped_item=l.pop()
        r_list.append(poped_item)
    return r_list

print(reversed_list(l))

