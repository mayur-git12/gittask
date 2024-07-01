# Ex1:-
names=['abdhish','bhavsar','abd']
print(max(names, key=lambda item: len(item)))

#EX2:-
student=[
    {'name':'abdhish','score':30,'age':20},
    {'name':'yuvraj','score':20,'age':21},
    {'name':'prem','score':10,'age':21}
]
print(max(student, key=lambda item:item.get('score'))['score'])

#Ex3:-
student2={
    'abdhish':{'score':30,'age':20},
    'yuvraj':{'score':20,'age':21},
    'prem':{'score':10,'age':23}
}
print(max(student2, key=lambda item:student2[item]['age']))