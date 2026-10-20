'''Given an array of integers and an integer K, find the length of the longest subarray whose sum is exactly K.'''

nums = [10, 5, 2, 7, 1, 9]
k = 15
maxLen = 0

prefix = {}
current_sum = 0

for i in range(len(nums)):
    
    current_sum += nums[i]
    
    if current_sum == k:
        maxLen = max(maxLen,i + 1)
    
    pre = current_sum - k
    if pre in prefix:
        length = i - prefix[pre]
        maxLen = max(maxLen,length)
        
    if current_sum not in prefix:
        prefix[current_sum] = i
        
print(maxLen)