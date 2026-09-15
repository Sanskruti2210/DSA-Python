"""
Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
a, b, c, d are all distinct valid indices of nums.
nums[a] + nums[b] + nums[c] + nums[d] == target.
Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets.
The output and the quadruplets can be returned in any order.
"""

# Better Approach
nums = [1, -2, 3, 5, 7, 9]
target = 7
ans = set()

for i in range(len(nums)):
    
    # Create a hashmap
    hashmap = set()
    
    for j in range(i + 1, len(nums)):
        
        for k in range(j + 1, len(nums)):
            
            # As nums[i] + nums[j] + nums[k] + nums[l] = target then 
            # nums[l](req) = target - nums[i] - nums[j] -nums[k]
            req = target - (nums[i] + nums[j] + nums[k])

            # if req is already in hashmap check it for duplicate
            if req in hashmap:
                quadraplet = tuple(sorted([nums[i], nums[j], nums[k], req]))
                ans.add(quadraplet)

            # Add it into hashmap
            hashmap.add(nums[k])

for item in ans:
    print(list(item), end=" ")
