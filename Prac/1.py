'''Given a sorted integer array nums, remove the duplicates in-place so that each unique element appears only once.

Return the number of unique elements.'''

nums = [1, 1, 2, 2, 3, 4, 4]

freq = {}
unique = 0
n = len(nums) - 1

for i in range(len(nums)):
    
    if nums[i] in freq:
        unique += 1
        nums[i],nums[n] = nums[n],nums[i]
        n -= 1
        print(nums)
    
    freq[nums[i]] = freq.get(nums[i],0) + 1
    
nums.reverse()
nums = nums[:unique]
nums.reverse()
print(unique)
print(nums)
    