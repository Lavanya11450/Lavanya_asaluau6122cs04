def linear_Search(list1, n, key):  
  
    
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5,457, 4,67,56,45, 7, 9]  
key = 67
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)