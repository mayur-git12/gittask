#here * perform operations we can write anything insteed of args
def all_total(*args):
    total=0
    for  num in args:
        total += num
    return total
print(all_total(1,2,3))

