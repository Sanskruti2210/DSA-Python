'''Given a binary array containing only 0 and 1, find the maximum number of consecutive 1s.'''

nums = [1, 1, 0, 1, 1, 1]

count1s = 0
max1s = 0

for i in range(len(nums)):
    
    if nums[i] == 1:
        count1s += 1
    elif nums[i] == 0:
        count1s = 0
        
    max1s = max(max1s,count1s)
        
print(max1s)