'''Given a sorted integer array nums, remove the duplicates in-place so that each unique element appears only once.

Return the number of unique elements.'''

nums = [1, 1, 2, 2, 3, 4, 4]

left = 1

for right in range(1, len(nums)):
    
    if nums[right] != nums[left - 1]:
        nums[left] = nums[right]
        left += 1
        
    print(nums)

print(left)
print(nums[:left])