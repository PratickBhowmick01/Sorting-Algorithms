#Merge sort
def merge(A,l,mid,r): 
    i,k = l,l
    j = mid+1
    B = [0]*len(A) 
    
    while(i <= mid and j <= r):
        if(A[i] <= A[j]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    
    if(i > mid):
        while(j <= r):
            B[k] = A[j]
            j += 1
            k += 1    
    else:
        while(i <= mid):
            B[k] = A[i]
            i += 1
            k += 1
    
    for k in range(l,r+1): 
        A[k] = B[k]

def mergeSort(A,l,r): 
    if (l < r):
        mid = (l+r) // 2
        mergeSort(A,l,mid)
        mergeSort(A,mid+1, r)
        merge(A,l,mid,r)

array = [-4,0,7,3,46,676, 454,10, 55, 6] 
mergeSort(array,0,len(array)-1) 
print(array)

# Time complexities-
# i) Best case: Ω(n log(n))
# ii) Worst case: θ(n log(n))
# iii) Average case: O(n log(n))
