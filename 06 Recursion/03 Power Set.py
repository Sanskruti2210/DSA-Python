'''
Given an array of integers nums of unique elements. 
Return all possible subsets (power set) of the array.
Do not include the duplicates in the answer.
'''

nums = [1, 2, 3]

n = len(nums)
res = []

for num in range(2**n):
    
    subset = []
    
    for j in range(n):
        
        if num & (1 << j):
            subset.append(nums[j])
            
    res.append(subset)
            
print(res)
            