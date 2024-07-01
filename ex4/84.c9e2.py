def numtostr(l):
    return [str(i) for i in l if(type(i)==int or type(i)==float)]
print(numtostr([True,False,1,1.0,3,[1,2,3]]))