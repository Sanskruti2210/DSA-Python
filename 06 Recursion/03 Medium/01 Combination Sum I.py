'''
Provided with a goal integer target and an array of unique integers nums, provide 
a list of all possible combinations of nums in which the selected numbers add up to the target. 
The combinations can be returned in any order.
A number may be selected from nums an infinite number of times. There are two distinct 
combinations if the frequency of at least one of the selected numbers differs.
The test cases are created so that, for the given input, there are fewer than 150 
possible combinations that add up to the target.
If there is no possible combination, then return an empty list.
'''

def CombinationSum(index,n,nums,arr,target,sum,res):
        
    # If we found targeted sum store it in res
    if sum == target :
        res.append(arr)
        return 
        
    # If sum > target return
    if index == n or sum > target :
        return

    # Pick for pick use index as one index can be picked more than one times
    CombinationSum(index,n,nums,arr + [nums[index]],target,sum + nums[index],res)
    
    # Not Pick
    CombinationSum(index + 1,n,nums,arr,target,sum,res)
    
nums = [2, 3, 5, 4]
target = 7
arr = []
res = []
n = len(nums)
CombinationSum(0,n,nums,arr,target,0,res)
print(res)

