def outer_fun(msg):
    def inner_fun():
        print( f"msg is {msg}")
    return inner_fun

var=outer_fun("hello")
var()
    
#Ex2:-
def to_power(x):
    def cal_power(n):
        return n**x
    return cal_power

cube=to_power(3)
print(cube(2))