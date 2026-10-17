'''
Implement Selection Sort to sort an array in increasing order.
'''

nums = [64, 25, 12, 22, 11]

for i in range(len(nums)):
    
    for j in range(i,len(nums)):
        
        if nums[i] > nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
            
print(nums)
        