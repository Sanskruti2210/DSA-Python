'''Given an array, find the element having the second-highest frequency.'''

nums = [1, 1, 2, 2, 2, 3, 3, 4]

freq = {}

for num in nums:
    
    freq[num] = freq.get(num,0) + 1
    

max_freq = max(freq,key = lambda x : freq[x])
max_key = [val for key,val in freq.items() if val == max_freq]

print(max_freq,max_key)