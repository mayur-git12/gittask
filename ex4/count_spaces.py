# count=0
# line="Codespeedy Technology Private Limited"
# for i in line:
#    if(i.isspace()):
#        count=count+1
# print(f"words in string:{count+1} ")

# a=input("Enter the value: ")
# s=a.count(' ')
# print(f'words:{s+1}')



# test_string = "Geeksforgeeks    is best Computer Science Portal"  
# print ("The original string is : " +  test_string) 
# res = len(test_string.split()) 
# print ("The number of words in string are : " +  str(res))


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))