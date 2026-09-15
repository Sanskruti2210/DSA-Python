"""
Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
a, b, c, d are all distinct valid indices of nums.
nums[a] + nums[b] + nums[c] + nums[d] == target.
Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets.
The output and the quadruplets can be returned in any order.
"""

# Optimise
nums = [1, -2, 3, 5, 7, 9]
target = 7

# Sort array
nums.sort()
ans = []

n = len(nums)
for i in range(n):

    # If i value is equal to it's previous one skip
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1, n):
        
        # If j value is equal to it's previous one skip
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        left = j + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[j] + nums[left] + nums[right]
            
            # If we find total append it into ans
            if total == target:
                ans.append([nums[i], nums[j], nums[left], nums[right]])
                left += 1
                right -= 1

                # If j value is equal to it's previous one skip
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                    
                # If j value is equal to it's previous one skip
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            # Else increase left
            elif total < target:
                left += 1
            
            # Else decrease right
            else:
                right -= 1

print(ans)
