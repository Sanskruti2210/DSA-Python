'''Given an integer array, find the maximum sum of a contiguous subarray.'''

nums = [-5,-2,-8]

i = 0
sum = 0
max_sum = float('-inf')

while i < len(nums):
    
    sum += nums[i]
    
    max_sum = max(max_sum,sum)
    
    if sum < 0:
        sum = 0
            
    
    i += 1
    
print(max_sum)
    