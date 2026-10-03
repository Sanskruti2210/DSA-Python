'''
Given an integer array nums, which can have duplicate entries, provide the power set.
Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.
'''

def subset(index,nums,arr,n,res):
    
    if index == n :
        
        # Handle duplicates
        arr = sorted(arr)
        
        if arr not in res:
        
            res.append(arr)
        return
    
    # Pick
    subset(index + 1,nums,arr + [nums[index]],n,res)
    
    # Not Pick
    subset(index + 1,nums,arr,n,res)
    
nums = [1, 3, 3]
arr = []
res = []
subset(0,nums,arr,len(nums),res)
print(sorted(res))
