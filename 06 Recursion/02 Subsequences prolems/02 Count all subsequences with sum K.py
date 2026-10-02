'''
Given an array nums and an integer k. Return true if there exist subsequences such that 
the sum of all elements in subsequences is equal to k else false.
'''

def SubSum(index,nums,arr,n,k,sum):
    
    count = 0
    
    # Base case
    if index == n:
        
        if sum == k:
            
            return 1
        
        return 0
      
    # Pick index  
    arr.append(nums[index])
    pick_res = SubSum(index + 1,nums,arr,n,k,sum + nums[index])
    
    count += pick_res
     
    # For not pick first remove the element that is picked before   
    arr.pop()
    
    # Not pick 
    not_pick_res = SubSum(index + 1,nums,arr,n,k,sum)
    
    count += not_pick_res
        
    return count
        
nums = [1, 2, 3, 4, 5]
k = 8
res = SubSum(0,nums,[],len(nums),k,0)
print(res)