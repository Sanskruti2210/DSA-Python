'''Given an integer array, find the contiguous subarray having the maximum sum.'''

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

ans = []

max_sum = 0
current_sum = 0 
best_start = 0
best_end = 0

for i in range(len(nums)):
    
    current_sum += nums[i]
    
    if current_sum < 0:
        best_end = i
        
    best_start = i
        
for i in range(best_start,best_end + 1):
    
    ans.append(nums[i])
    
print(ans)