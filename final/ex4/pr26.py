l1 = [1,2, 3, 4,5, 6,7, 8,9,10] 
l2 = [11,12,13,14,15,16,17,18,19,20] 
  
# printing original lists 
print ("Original list 1 : " + str(l1)) 
print ("Original list 2 : " + str(l2)) 
  
# using naive method to  
# add two list  
res_list = [] 
for i in range(0, len(l1)): 
    res_list.append(l1[i] + l2[i]) 
# printing resultant list  
print ("Resultant list is : " + str(res_list)) 

# l1=[1,2,3]
# l2=[10,20,30]
# t=[]
# lc=[t:=l1[i]+l2[i] for i in range(0,len(l1))]
# print(lc)