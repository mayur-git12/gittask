dict1={'a':1,'b':2,'c':3}
dict2={'a':4,'d':5,'e':6}

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

dict3=print(Merge(dict1, dict2))
