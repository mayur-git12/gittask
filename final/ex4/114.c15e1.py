def even_grn(n):
    for num in range(1,n+1):
        if num%2==0:
            yield(num)
print(even_grn(5))

for num in even_grn(7):
    print(num)