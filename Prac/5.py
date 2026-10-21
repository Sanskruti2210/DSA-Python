'''Given a sorted array that has been rotated at some unknown position, search for target.

Return its index, or -1 if it doesn't exist.'''

def IStarget(nums,target):
    
    low = 0
    high = len(nums) - 1
    
    while low <= high :
        
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[low] < nums[mid]:
            
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else :
                low = mid + 1
                
        elif nums[mid] < nums[high]:
            
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else :
                high = mid - 1
                
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
res = IStarget(nums,target)
print(res)