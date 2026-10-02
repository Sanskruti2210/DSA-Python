'''
Given an array nums and an integer k. Return true if there exist subsequences such that 
the sum of all elements in subsequences is equal to k else false.
'''

def SubSum(index,nums,arr,n,k,sum):
    
    # Base case
    if index == n:
        
        if sum == k:
            
            return True
        
        return False
      
    # Pick index  
    arr.append(nums[index])
    pick_res = SubSum(index + 1,nums,arr,n,k,sum + nums[index])
    
    if pick_res :
        return True 
     
    # For not pick first remove the element that is picked before   
    arr.pop()
    
    # Not pick 
    not_pick_res = SubSum(index + 1,nums,arr,n,k,sum)
    
    if not_pick_res:
        return True
        
    return False
        
nums = [1, 2, 3, 4, 5]
k = 8
res = SubSum(0,nums,[],len(nums),k,0)
print(res)