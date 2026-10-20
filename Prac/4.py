'''Given an array of integers, find the element that appears more than n/2 times.

You may assume such an element always exists.'''

freq = {}

nums = [2, 2, 1, 1, 1, 2, 2]
n = len(nums)

for num in nums:
    
    freq[num] = freq.get(num,0) + 1
    
ans = [key for key,val in freq.items() if val > (n//2)]
print(ans[0])