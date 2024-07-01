# Genrators are iterators
def nums(n):
    for i in range(1,n+1):
        yield(i)
print(nums(10))

# for numbers in nums(10):
#     print(numbers)