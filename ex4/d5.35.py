import random

arr = random.sample(range(1, 100), 25)
print(arr)

def bubbleSort(arr): 
    n = len(arr) 
  
   
    for i in range(n-1): 
   
        for j in range(0, n-i-1): 
  
        
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  

  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 