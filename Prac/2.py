'''Given an integer array, find the smallest element without using min().'''

nums = [5, 2, 8, 1, 9]

min_ele = nums[0]

for n in nums:
    
    if n < min_ele:
        min_ele = n
        
print(min_ele)