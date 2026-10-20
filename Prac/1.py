'''Given an integer array nums and an integer target, return the indices of the two numbers whose sum equals target.

You may assume exactly one solution exists.'''

nums = [2, 7, 11, 15]
target = 9

count = {}

for i in range(len(nums)):
    
    exist = target - nums[i]
    
    if exist in count:
        print([count[exist],i])
        break
    
    count[nums[i]] = i
    
    