"""
Given an integer array nums of size n containing values from [1, n] and each value
appears exactly once in the array, except for A, which appears twice and B which is missing.
Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
Note: You are not allowed to modify the original array.
"""

nums = [3, 5, 4, 1, 1]
freq = {}
ans = []

for num in nums:
    if num not in freq:
        freq[num] = 1
    else:
        freq[num] += 1

ans = [key for key, value in freq.items() if value > 1]
for i in range(1, len(nums) + 1):
    if i not in freq:
        ans.append(i)
print(freq)
print(ans)
