'''You are given an array containing N distinct numbers from 0 to N. Exactly one number is missing. Find it.'''

nums = [3, 0, 1]

xor = len(nums)

for i in range(len(nums)):
    xor ^= i
    xor ^= nums[i]

print(xor)