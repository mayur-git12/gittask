# Perform following operations for this string :
# a) Replace “I am” with “we are”
# b) count the no. of occurrences of letter ‘e’ in the string.
# c) Is there any word repeated in this string ?
# d) What is there on the 10th position in the string ?


dic = 'This time I am going to pass this test.'

print(dic.replace('I am','we are'))

print(dic[9])

print(dic.count('e'))


temp=""
for i in range(len(dic)):
    if dic[i] not in temp:
        
        temp=temp+dic[i]
        # print(f"{dic[i]}:{dic.count(dic[i])}")
        if dic.count(dic[i])>1:
            print(f'repeated characters:{dic[i]}')
            
        



