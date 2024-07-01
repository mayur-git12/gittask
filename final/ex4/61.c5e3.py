def reversed_elements(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements
words=['abd','bha','urv']
print(reversed_elements(words))