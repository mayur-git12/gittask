def fun(l,**kwargs):
    if kwargs.get('revers_str')==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
        
l=['abdhish','bhavsar','abdba']
print(fun(l,revers_str=True))