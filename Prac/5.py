'''Given an integer array nums that may contain duplicate elements, generate its power set.
The result must not contain duplicate subsets.'''

def subSet(index,nums,n,arr,res):
    
    if index == n:
        
        arr = sorted(arr)
        
        if arr not in res:
            res.append(arr)
        
        return
    
    # Not pick
    subSet(index + 1,nums,n,arr,res)
    
    # Pick
    subSet(index + 1,nums,n,arr + [nums[index]],res)


nums = [1, 2, 2]
res = []
arr = []
subSet(0,nums,len(nums),arr,res)
res.sort()
print(res)