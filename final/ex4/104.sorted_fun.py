guitars=[
    {'modle':'a','price':3000},
    {'modle':'b','price':2000},
    {'modle':'c','price':5000},
    {'modle':'d','price':3500}
]
print(sorted(guitars,key=lambda item: item['price']))