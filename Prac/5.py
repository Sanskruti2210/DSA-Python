'''Given an array of integers, rearrange it into the next lexicographically greater permutation.

If the next permutation does not exist, rearrange it into the smallest possible order.'''

nums = [1, 2, 3]

breakpoint = -1

for i in range(len(nums) - 2,-1,-1):
    
    if nums[i]  < nums[i + 1]:
        
        breakpoint = i
        break
    
print(breakpoint)
if breakpoint == -1:
    nums.reverse()
else:
    
    for j in range(len(nums) - 1,breakpoint,-1):
        
        if nums[j] > breakpoint:
            nums[j],nums[breakpoint] = nums[breakpoint],nums[j]
            
    nums[breakpoint + 1 : ] = reversed(nums[breakpoint + 1:])
    
print(nums)