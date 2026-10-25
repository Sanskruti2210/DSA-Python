'''Given an array, count the number of inversions.

An inversion is a pair (i, j) such that:
i < j
nums[i] > nums[j]'''

nums = [5, 3, 2, 4, 1]
count = 0

for i in range(len(nums)):
    
    for j in range(i,len(nums)):
        
        if i < j  and nums[i] > nums[j]:
            count += 1
            
print(count)