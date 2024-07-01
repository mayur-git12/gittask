name=input("enter name:")
def palindrom(word):
    reversedword=word[::-1]
    if word==reversedword:
        return True
    return False
print(palindrom(f"{name}"))

# s=input('enter name')
# ns=s[::-1]
# if s==ns:
#     print('palindom')

# else:
#     print('not palindrom')