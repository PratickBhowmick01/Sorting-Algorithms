#INSERTION SORT
def insertionSort(a):
    for i in range(1, len(a)):
        value = a[i]
        j = i-1
        while(j >= 0):
            if (value < a[j]):
                a[j+1],a[j] = a[j],value
                j -= 1
            else:
                break
array = [5,4,3,2,1]
insertionSort(array)
print(array)

# Time complexities-
# i) Best case: Ω(n)
# ii) Worst case: θ(n²)
# iii) Average case: O(n²)