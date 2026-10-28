'''Given an integer array, find all elements that appear more than ⌊n/3⌋ times.'''

nums = [3, 2, 3]
n = len(nums)

freq = {}

for num in nums:
    
    freq[num] = freq.get(num,0) + 1
    
ans = [key for key,val in freq.items() if val > (n//3)]
print(ans[0])