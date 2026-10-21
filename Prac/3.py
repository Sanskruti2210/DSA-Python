'''Every element in an integer array appears twice except one element. Find the element that appears only once.'''

nums = [4, 1, 2, 1, 2]

count = {}

for i in range(len(nums)):
    
    count[nums[i]] = count.get(nums[i],0) + 1
    
ans = [key for key,val in count.items() if val == 1]
print(ans[0])


XOR = 0

for i in range(len(nums)):
    
    XOR ^= nums[i]
        
print(XOR)