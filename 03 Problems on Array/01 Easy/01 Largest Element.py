"""
Given an array of integers nums, return the value of the largest element in the array
"""

nums = [1, 5, 42, 11, 56]
largest = nums[0]

for i in range(len(nums)):

    # Store 1st element as largest if we find any other larger element than replace
    # it then compare again for next iteration
    if nums[i] > largest:
        largest = nums[i]

print(largest)
