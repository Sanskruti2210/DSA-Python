'''Given an integer array nums and an integer K, count the number of subarrays whose sum is exactly K.'''

nums = [1, 2, 3]
k = 3

prefix = {0 : 1}
current_sum = 0
count = 0

for i in range(len(nums)):
    
    current_sum += nums[i]
    
    if current_sum == k:
        count += 1
        
    pre = k - current_sum
    if pre in prefix:
        count += 1
        
    prefix[current_sum] = i
        
print(count)