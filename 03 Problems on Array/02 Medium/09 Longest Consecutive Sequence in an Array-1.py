"""
Given an array nums of n integers.
Return the length of the longest sequence of consecutive integers.
The integers in this sequence can appear in any order.
"""

nums = [100, 4, 200, 1, 3, 2]

# First sort the array
nums.sort()
lastSmaller = nums[0]
count = 1
maxLen = 0
print(nums)

# IMPORTANT : If an element is not in consecutive sequence then it can start the new sequence
for i in range(1, len(nums)):

    # If current element is exactly 1 greater than the previous one,
    # it is part of the same consecutive sequence
    if nums[i] == (lastSmaller + 1):
        count += 1
        lastSmaller = nums[i]

    # If it is not consecutive, the previous sequence ends
    # and we start counting a new sequence
    else:
        maxLen = max(maxLen, count)
        count = 1
        lastSmaller = nums[i]

print(maxLen)
