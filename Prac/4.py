'''Given a sorted array and a target X, find the index of X using Binary Search.'''

def binarySearch(nums,x):
    
    low = 0
    high = len(nums) - 1
    
    if low > high:
        return -1
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
            
nums = [1, 3, 5, 7, 9]
x = 7
print(binarySearch(nums,x))

