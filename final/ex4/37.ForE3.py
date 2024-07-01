name=input("enter bane:")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        
        temp=temp+name[i]
        print(f"{name[i]}:{name.count(name[i])}")

