'''
Given an array nums of n integers. Return array of sum of all subsets of the array nums.
Output can be returned in any order.
'''

def subset(index,nums,n,sum,res):
    
    if index == n :
        
        res.append(sum)
        return
    
    # Pick
    subset(index + 1,nums,n,sum + nums[index],res)
    
    # Not Pick
    subset(index + 1,nums,n,sum,res)
    
nums = [5, 2, 1]
res = []
subset(0,nums,len(nums),0,res)
print(sorted(res))
