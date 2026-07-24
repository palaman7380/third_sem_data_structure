
def sortArray(nums):
    n= len(nums)
    for i in range(n):
        isswap = False
        for j in range(n-i-1):
            if nums[j]> nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                isswap = True
            if not isswap:
                break

        return nums

nums = [1,3,2,4,5,6]
print(sortArray(nums))