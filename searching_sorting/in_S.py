def sortArray(arr):
    
    n= len(arr)
    for i in range(n-1):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key

    return arr


print(sortArray([1,3,2,4,65,788,77,66,46]))

