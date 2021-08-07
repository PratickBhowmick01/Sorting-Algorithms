#Quick Sort
def Partition(A,p,q):
    i,x = p,A[p]        #pivot is A[p]
    
    for j in range(p+1,q+1):
        if(A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[p],A[i] = A[i],A[p]
    return i 
    
def quickSort(A,p,r):
    if(p < r):
        q = Partition(A, p, r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

array = [15,-4,0,7,3,46,676, 454,10, 55, 6] 
quickSort(array,0,len(array)-1)  
print(array)


# Time complexities-
# i) Best case: Ω(n log(n))
# ii) Worst case: θ(n log(n))
# iii) Average case: O(n^2)

