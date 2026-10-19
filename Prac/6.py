'''Given an integer array, determine whether it is sorted in non-decreasing order.'''

nums = [1, 3, 2, 4]

isSorted = True

for i in range(1,len(nums)):
    
    if nums[i - 1] > nums[i]:
        isSorted = False
        break
    
print(isSorted)