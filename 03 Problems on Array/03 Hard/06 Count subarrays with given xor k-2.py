"""
Given an array of integers nums and an integer k,
return the total number of subarrays whose XOR equals to k.
"""

nums = [4, 2, 2, 6, 4]
k = 6
n = len(nums)
current_XOR = 0
count = 0
freq = {}

for i in range(n):

    current_XOR ^= nums[i]
    
    # If current_XOR = k increase count
    if current_XOR == k:
        count += 1

    # XOR = nums[i]^nums[j] so check for target = current_XOR^k freq
    target = current_XOR ^ k
    if target in freq:
        count += freq[target]

    # If it is not in freq make count = 1
    if current_XOR not in freq:
        freq[current_XOR] = 1
        
    # Else increase the count
    else:
        freq[current_XOR] += 1

print(count)
