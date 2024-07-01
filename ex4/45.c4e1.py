num1,num2=input("enter 2 num:").split(",")

def gretter(a,b):
    
    if a>b:
        return a
    else:
        return b
#bigger=gretter(int(num1),int(num2))   
#print(f"{bigger} is gretter") 
print(f"{gretter(int(num1),int(num2))}")       




