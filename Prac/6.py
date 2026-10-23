'''Given an unsorted array, find the length of the longest sequence of consecutive integers.'''

nums = [1,2,3,4,100,101,102,103,104,105]

nums.sort()
nums = list(set(nums))

longest = 1
max_longest = 0

i = 1
while i < len(nums):
    
    while i < len(nums) and nums[i] == nums[i - 1] + 1:
        longest += 1
        i += 1
        
    max_longest = max(max_longest,longest)
    print(longest)
        
    longest = 1
        
    i += 1
    
print(max_longest)
    
        
    