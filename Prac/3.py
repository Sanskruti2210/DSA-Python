'''
Implement Insertion Sort using recursion.
Restrictions:
- Do not use a for loop.
- Do not use a while loop.
'''

def recursiveInsertionSort(nums,j):
    
    if j == 0:
        return
    
    if nums[j - 1] > nums[j]:
        
        nums[j - 1],nums[j] = nums[j],nums[j - 1]
        
        recursiveInsertionSort(nums,j + 1)
            
nums = [5, 3, 4, 1, 2]
recursiveInsertionSort(nums,0)
print(nums)
        