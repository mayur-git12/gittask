# Ask user to enter the birthdate and give output for the following :
# a. How old the user is ?
# b. Is a user Adult or Child ?
# c. Will user be able to take retirement next year on the same day as of today ?
# (Assume that retirement is allowed at 59 years)


# by=int(input('by'))
# cy=int(input('cy'))





# print(f'age is{cd-bd}-{cm-bm}-{cy-by}')


from datetime import date
  
# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day))
#     return age
    
    

# print(calculateAge(date(1999, 2, 3)))

# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day))
#     if age>=18:
#         print('adult')
#     else:
#         print('child')
    
# print(calculateAge(date(1999, 2, 3)))

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day))
    if age==58:
        print('you can take retirement next year')
    else:
        print('cant take retirement')
    
    
print(calculateAge(date(1999, 2, 3)))
    













