"""
Given an integer array nums. Return all triplets such that:
i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets.
The output and the triplets can be returned in any order.
"""

# Optimal Approach
nums = [-1, 0, 1, 2, -1, -4]
nums.sort()

ans = []
n = len(nums)

for i in range(n):

    # If i is equal to it's previous value then skip
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:

        total = nums[i] + nums[left] + nums[right]

        # If total == 0 add it into ans
        if total == 0:
            ans.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1

            # If left it is equal to it's previos value continue
            while left < right and nums[left] == nums[left - 1]:
                left += 1
                
            # If right it is equal to it's previos value continue
            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        # Else increase left
        elif total < 0:
            left += 1
            
        # Else decrease right
        else:
            right -= 1

for item in ans:
    print(item, end="\n")
