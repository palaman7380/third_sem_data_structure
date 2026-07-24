def sortArray(arr):
    n= len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j]< arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i],arr[min_idx] = arr[min_idx], arr[i]
                
    return arr

arr = [1,3,2,4,5]
print(sortArray(arr))



