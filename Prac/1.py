'''Given an array of integers, find the element that occurs the maximum number of times.'''

nums = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for num in nums:
    
    freq[num] = freq.get(num,0) + 1
    
max_freq = max(freq ,key = lambda x : freq[x])
print(max_freq)