"""
Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.
"""

def rotateArr(nums, n):

    # If n = 0 all rotation is completed base case
    if n == 0:
        return

    # Copy the first element into var as while rotating the 0th indexed element will get overwrite
    temp = nums[0]

    # Rotate every index left
    for ele in range(1, len(nums)):
        nums[ele - 1] = nums[ele]

    # The last element will be the first indexed element
    nums[-1] = temp

    rotateArr(nums, n - 1)

nums = [1, 2, 3, 4, 5, 6]
rotateArr(nums, 1)
print(nums)
