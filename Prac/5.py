'''Given an array and a target, return the index of the target. Return -1 if it doesn't exist.'''

nums = [4, 7, 2, 9, 5]
target = 9

isFound = -1

for i in range(len(nums)):
    
    if nums[i] == target:
        isFound = i
        
print(isFound)