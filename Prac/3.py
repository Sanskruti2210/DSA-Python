'''Given an integer array, move all 0s to the end while maintaining the relative order of the non-zero elements.

Do it in-place.'''

nums = [0, 1, 0, 3, 12]

left = 0

for right in range(len(nums)):
    
    if nums[right] != 0:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
    
print(nums)