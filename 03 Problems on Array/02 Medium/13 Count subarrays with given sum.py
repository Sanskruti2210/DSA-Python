"""
Given an array of integers nums and an integer k,
return the total number of subarrays whose sum equals to k.
"""

nums = [1, 2, 3, 3]
k = 3

prefix = {}
current_sum = 0
count = 0

for i in range(len(nums)):

    current_sum += nums[i]

    # If current_sum itself is k, then subarray from 0 to i
    # has sum k
    if current_sum == k:
        count += 1

    # If an earlier prefix sum = current_sum - k,
    # then the elements between that prefix and current index
    # have sum k
    pre = current_sum - k

    if pre in prefix:
        count += prefix[pre]

    # Store how many times this prefix sum has appeared
    prefix[current_sum] = prefix.get(current_sum, 0) + 1


print(count)
print(prefix)
