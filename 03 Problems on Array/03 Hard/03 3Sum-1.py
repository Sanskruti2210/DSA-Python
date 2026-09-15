"""
Given an integer array nums. Return all triplets such that:
i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets.
The output and the triplets can be returned in any order.
"""

# Brute Force
nums = [-1, 0, 1, 2, -1, -4]
triplet = []
ans = set()

for i in range(len(nums)):
    
    for j in range(i + 1, len(nums)):
        
        for k in range(j + 1, len(nums)):
            
            if i != j != k and nums[i] + nums[j] + nums[k] == 0:
                
                # Use tuple because list can't be add into set
                triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                ans.add(triplet)

ans = list(ans)
for item in ans:
    print(list(item))
