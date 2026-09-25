'''
Given an array of n integers, find the second most frequent element in it.
If there are multiple elements that appear second most frequent times, find the smallest of them.
If second most frequent element does not exist return -1.
'''

arr = [1, 2, 2, 3, 3, 3]

freq = {}

for num in arr:
    
    freq[num] = freq.get(num,0) + 1
    
max_freq = max(freq.values())
max_key = 0

for key,val in freq.items():
    
    if val == max_freq:
        max_key = key
    
ans_key = float('inf')
ans_value = float('-inf')

for key,val in freq.items():
    
    # Check if given value is lesser than max_freq
    if val < max_freq:
        
        # current val is greater than ans
        if val > ans_value:
            ans_key = key
            ans_value = val
            
        # If it is same store the minimum key 
        elif val == ans_value and key < ans_key:
            ans_key = key

print(ans_key)