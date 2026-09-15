"""
Given an array nums of size n and an integer k,
find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
"""

nums = [10, 5, 2, 7, 1, 9]

k = 15

left = 0
right = 0

n = len(nums)
max_len = 0
sum = nums[0]

# Use sliding window pattern
while right < n:

    # If sum is greater than k then start reducing element from left
    # For example : nums = [10,5,2,7,1,9]
    # 10 < 15 => window = [10]
    # 10 + 5 = 15 == 15 => window = [10,5] => record this and in len = 1 - 0 + 1 = 2 max_len = max(0,2) = 2
    # 15 + 2 = 17 > 15 => window = [5,2] (reduce element from left) => sum = 17 - 10 = 7
    # 7 + 7 = 14 < 15 => window = [5,2,7]
    # 14 + 1 = 15 == 15 => window = [5,2,7,1] => max_len = 4 - 1 + 1 = 4 max_len = max(2,4) = 4
    # 15 + 9 = 24 > 15 => window = [2,7,1,9] => sum = 24 - 5 = 19
    # 19 > 15 => window = [7,1,9] => sum = 19 - 2 = 17
    # 17 > 15 => window = [1,9] => sum = 17 - 7 = 10
    # END because right + 1 = 6 > 5 so Stop
    while left <= right and sum > k:
        sum -= nums[left]
        left += 1

    # When we find some record it means store the max_len sum
    if sum == k:
        max_len = max(max_len, right - left + 1)

    # increase right and add elements in window
    right += 1
    if right < n:
        sum += nums[right]

print(max_len)
