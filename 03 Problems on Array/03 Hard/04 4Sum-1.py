"""
Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
a, b, c, d are all distinct valid indices of nums.
nums[a] + nums[b] + nums[c] + nums[d] == target.
Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets.
The output and the quadruplets can be returned in any order.
"""

# Brute Force
nums = [1, -2, 3, 5, 7, 9]
target = 7
ans = set()
n = len(nums)

for i in range(n):
    
    for j in range(i + 1, n):
        
        for k in range(j + 1, n):
            
            for l in range(k + 1, n):
                
                if nums[i] + nums[j] + nums[k] + nums[l] == target:
                    
                    # Use tuple because list can't be add into set
                    quadraplet = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                    ans.add(quadraplet)

for item in ans:
    print(list(item), end=" ")
