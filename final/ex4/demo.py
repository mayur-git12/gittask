student = {
    "name" : " rahul",
    "subject" : {
        "phy" :56,
        "chem" : 36,
        "math" : 25 
     }
}


#print(student.items())
#print (student.keys())

#print(student["name3"])
#print(student.get("name"))

student.update({"city":"delhi"})
print(student)