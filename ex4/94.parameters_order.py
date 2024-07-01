# fuction with all parameters:-
def fun(name,*args,last_name='bhavsar',**kwargs):
    print(name)                                #normal parameter
    print(args)                                #args parameter
    print(last_name)                           #Default parameter
    print(kwargs)                              #kwargs parameter

fun('abdhish',1,2,3,a=1,b=2)
