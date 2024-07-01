# pop method:-
f1=['apple','mengo','kiwi']      #if we dosent consider position then it DEL last Element 
f1.pop(1)
print(f1)

# Del method:-
f2=['apple','mengo','kiwi'] 
del f2[0]                       # we have to consider position in this method
print(f2)

#remove method:-
f3=['apple','mengo','kiwi','apple'] 
f3.remove('apple')                 #if multiple same elements are thir then it removes only 1
print(f3)                              #considerd element is not in list(error)