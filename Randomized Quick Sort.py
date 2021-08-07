#Randomized Quick sort
import random

def Partition(A,p,q):
    i,x = p,A[p]        #pivot is A[p]
    
    for j in range(p+1,q+1):
        if(A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[p],A[i] = A[i],A[p]
    return i 

def randomizedPartition(A,p,r):
    i = random.randint(p,r)     
    A[p], A[i] = A[i], A[p] 
    return Partition(A,p,r) 
    
def randomizedQuickSort(A,p,r):
    if(p < r):
        q = randomizedPartition(A, p, r) 
        randomizedQuickSort(A,p,q-1)
        randomizedQuickSort(A,q+1,r)  

array = [-4,0,7,3,46,676, 454,10, 55, 6] 
randomizedQuickSort(array,0,len(array)-1) 
print(array)

# Time complexities-
# i) Best case: Ω(n log(n))
# ii) Worst case: θ(n log(n))
# iii) Average case: O(n^2)


