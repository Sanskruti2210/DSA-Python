'''Given an integer array nums, find the largest element in the array.'''

nums = [2, 5, 1, 3, 0]

largest = nums[0]

for i in range(len(nums)):
    
    if nums[i] > largest:
        largest = nums[i]
        
print(largest)