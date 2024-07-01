name,age=input("enter your name and age:").split(",")
age=int(age)
#name=input("enter name:")
#age=input("enter age:")
if age==10 and (name[0]=="a" or name[0]=="A"):
    print("you can watch it")
else:
    print("you cant watch it")