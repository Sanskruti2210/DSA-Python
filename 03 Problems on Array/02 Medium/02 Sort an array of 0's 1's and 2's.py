"""
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
The sorting must be done in-place, without making a copy of the original array.
"""

nums = [1, 2, 2, 1, 0]
c0 = c1 = c2 = 0

# Count the num of 0s ,1s and 2s
for i in range(len(nums)):
    if nums[i] == 0:
        c0 += 1
    elif nums[i] == 1:
        c1 += 1
    else:
        c2 += 1

# Append 0 in original array
for i in range(c0):
    nums[i] = 0

# Append 1 in original array
for j in range(c0, c0 + c1):
    nums[j] = 1

# Append 2 in original array
for k in range(c0 + c1, c0 + c1 + c2):
    nums[k] = 2

# Suppose nums = [0,1,1,0,2]  ans = [0,0,1,1,2]
# So the 0 is at two index 0 and 1
# 1 is at two index 2 and 3
# 2 is at one index 4
# So the index of 2 depends on occurrence of 1
# Same as index of 1 depends on occurrence of 0

print(nums)
