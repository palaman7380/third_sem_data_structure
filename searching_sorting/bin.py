def binary_search_recursive(arr, target, left, right):
    
    if left > right:
        return -1
        
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search_recursive(numbers, 23, 0, len(numbers) - 1))  # Output: 5
