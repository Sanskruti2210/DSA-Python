'''
Given an array of integers nums, return the second-largest element.
'''
nums = [1, 5, 42, 67]
largest = nums[0]
secondLargest = -1

for i in range(len(nums)):
    
    if nums[i] > largest:
        secondLargest = largest
        largest = nums[i]
    elif nums[i] > secondLargest:
        secondLargest = nums[i]
        
print(secondLargest)