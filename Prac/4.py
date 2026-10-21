'''Given an array containing only 0, 1, and 2, sort it in ascending order.

Do not use Python's sort() or sorted().'''

nums = [2, 0, 2, 1, 1, 0]

c0 = c1  = c2 = 0

for i in range(len(nums)):
    
    if nums[i] == 0:
        c0 += 1
    elif nums[i] == 1:
        c1 += 1
    else :
        c2 += 1
        
for i in range(0,c0):
    nums[i] = 0
    
for j in range(c0,c0+c1):
    nums[j] = 1

for k in range(c0+c1,len(nums)):
    nums[k] = 2
    
print(nums)