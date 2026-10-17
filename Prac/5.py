'''Given an integer array, find the maximum sum of a contiguous subarray.'''

nums = [-2,1,-3,4,-1,2,1,-5,4]

i = 0
sum = 0
max_sum = float('-inf')

while i < len(nums):
    
    sum += nums[i]
    
    if sum < 0:
        sum = 0
        
    max_sum = max(max_sum,sum)    
    
    i += 1
    
print(max_sum)
    