'''Given an integer array nums and an integer k, rotate the array to the right by k positions.'''

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

nums.reverse()
nums = nums[k - 1::-1] + nums[:k - 1:-1]
print(nums)