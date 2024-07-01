num=input("Enter number:")

def armstrong(num):
    if len(num) == 1:
        arm = int(num[0])**3
    elif len(num) == 2:
        arm = int(num[0])**3+int(num[1])**3
    elif len(num) == 3:
        arm = int(num[0])**3+int(num[1])**3+int(num[2])**3
    return arm

if armstrong(num) == int(num):
    print('number is armstrong')
else:
    print('not arm')