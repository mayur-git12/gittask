# kwargs as args:-
def fun(**kwargs):
    print(kwargs)
fun(first_name='abd',last_name='bha')

#dict unpacking:-
def fun2(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")
d={'name':'abdhish','age':20}
fun2(**d)