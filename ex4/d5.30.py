import random

randomlist = random.sample(range(1,100), 15)
print(randomlist)
print(max(randomlist))

import functools 
import operator 
  
# using reduce to compute sum of list 
# using operator functions 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(operator.add,randomlist))