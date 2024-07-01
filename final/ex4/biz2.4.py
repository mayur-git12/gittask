s=input('string:')
d=l=0

for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print(f'latters:{l}')
print(f'digits:{d}')