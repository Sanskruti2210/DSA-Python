'''
Given an array of n integers, find the sum of the frequencies of the highest occurring number and 
lowest occurring number.
'''

arr = [1, 2, 2, 3, 3, 3]

freq = {}

for ele in arr:
    
    freq[ele] = freq.get(ele,0) + 1
    
max_freq = max(freq.values())
min_freq = min(freq.values())

print("Sum of highest and lowest freq : ", max_freq + min_freq)
        