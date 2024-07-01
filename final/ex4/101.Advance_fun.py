#def avg_finder(*args):
#    avg=[]
#    for pair in zip(*args):
#        avg.append(sum(pair)//len(pair))
#    return avg
#print(avg_finder([2,5,4],[3,4,1],[4,4,4]))

avg_finder = lambda *args:[sum(pair)//len(pair) for pair in zip(*args)]
print(avg_finder([2,5,4],[3,4,1],[4,4,4]))
