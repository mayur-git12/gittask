import random

randomlist = random.sample(range(1,100), 10)
print(randomlist)

is_even = lambda x: x % 2 == 0
  
lis2 = list(filter(is_even, randomlist)) 
  
print(lis2) 

is_odd = lambda x: x % 2 != 0
  
lis3 = list(filter(is_odd, randomlist)) 
print(lis3)