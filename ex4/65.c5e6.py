def sublistcounter(l):
    count=0
    for i in l:
        if type(i)==list:
            count=count+1
    return count
mixed=[1,2,3,[2,5],[6,8]]
print(sublistcounter(mixed))