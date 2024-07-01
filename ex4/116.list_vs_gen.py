# memory:-

l=[i**2 for i in range(1000000)]

g=(i**2 for i in range(1000000))

# Time:-

# import time
# t1=time.time()                                #List are faster than generators
# l=[i**2 for i in range(1000000)]
# t2=time.time()
# print(t2-t1)


import time
t1=time.time()
g=(i**2 for i in range(1000000))
t2=time.time()
print(t2-t1)