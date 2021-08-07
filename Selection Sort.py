#SELECTION SORT
def min_selection_sort(a):
    for i in range(len(a)-1):
        min_v = a[i]         
        min_idx = i              
        
        for j in range(i+1,len(a)):
            if(a[j] < min_v):   
                min_v = a[j]       
                min_idx = j                  

        a[i],a[min_idx] = min_v,a[i]  
        
array = [1,3,0,2,5,4] 
min_selection_sort(array)
print(array) 

# Time complexities-
# i) Best case: Ω(n²)
# ii) Worst case: O(n²) 
# iii) Average case: θ(n²)