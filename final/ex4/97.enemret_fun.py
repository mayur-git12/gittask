# We use Enumeret function with for loop to track position of our items in iterables

# How to do this without Enumeret function:-
#names=['a','b','c']
#pos=0
#for name in names:
#    print(f"{pos} --> {name}")
#    pos+=1

# With Enemret Function:-
names=['a','b','c']
for pos,name in enumerate(names):
    print(f"{pos} --> {name}")