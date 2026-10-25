'''Given an integer array, find the contiguous subarray having the maximum product.'''

nums = [2, 3, -2, 4]

prefix = 1
suffix = 1
max_prod = 0

n = len(nums)

for i in range(n):
    
    prefix *= nums[i]
    suffix *= nums[n - i - 1]
    
    max_prod = max(max_prod,prefix,suffix)
    
print(max_prod)