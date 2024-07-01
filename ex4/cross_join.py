l1=['a','b','c']
l2=['1','2','3']
l3=['ex','ara']

l4=[f'{a}{b}{c}' for a in l1 for b in l2 for c in l3]
print(l4)