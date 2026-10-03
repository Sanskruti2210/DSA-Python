'''
Given collection of candidate numbers (candidates) and a integer target.
Find all unique combinations in candidates where the sum is equal to the target.
There can only be one usage of each number in the candidates combination and 
return the answer in sorted order.
e.g : The combination [1, 1, 2] and [1, 2, 1] are not unique.
'''

def CombinationSum(index,n,nums,arr,target,sum,res):
        
    # If we found targeted sum store it in res
    if sum == target:
        
        arr = sorted(arr)
        
        if arr not in res : 
            res.append(arr)
            return 
        
    # If sum > target return
    if index == n or sum > target :
        return

    # Pick for pick use index as one index can be picked more than one times
    CombinationSum(index + 1,n,nums,arr + [nums[index]],target,sum + nums[index],res)
    
    # Duplicate handling
    next_index = index + 1
    
    while next_index < n and nums[next_index] == nums[index]:
        next_index += 1
    
    # Not Pick
    CombinationSum(next_index,n,nums,arr,target,sum,res)
    
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27
nums.sort()
arr = []
res = []
n = len(nums)
CombinationSum(0,n,nums,arr,target,0,res)
print(sorted(res))

