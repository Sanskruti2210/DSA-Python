'''Given an array containing 0s, 1s and 2s, sort it in-place without using a general-purpose sorting function.'''

nums = [2,0,2,1,1,0]
c0 = c1 = c2 = 0

for n in nums:
    if n == 0:
        c0 += 1
    elif n == 1:
        c1 += 1
    else:
        c2 += 1
        
for i in range(0,c0 + 1):
    nums[i] = 0
    
for j in range(c0,c0 + c1 + 1):
    nums[j] = 1
    
for k in range(c0 + c1,len(nums)):
    nums[k] = 2
    
print(nums)