"""
Given a binary array nums, return the maximum number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.
"""

nums = [1, 1, 0, 0, 1, 1, 1, 0]
count = 0
max_count = 0

for i in range(len(nums)):

    # nums[i] == 1 then increase the counter
    if nums[i] == 1:
        count += 1

    # Reset the counter if next element is not 1(or is 0)
    else:
        # store the max counter value between current and previous
        max_count = max(count, max_count)
        count = 0

print(max_count)
