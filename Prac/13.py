'''Given a collection of candidate numbers and an integer target, find all unique combinations whose sum equals target.
Rules:
- Each number can be used only once.
- The answer must not contain duplicate combinations.
- [1,2,2] and [2,1,2] are considered the same combination.'''

def combSum(index,candidates,target,sum,n,arr,res):
    
    if sum == target:
        
        arr = sorted(arr)
        
        if arr not in res:
            
            res.append(arr)
            
        return 
    
    if index == n:
        return
    
    combSum(index + 1,candidates,target,sum + candidates[index],n,arr + [candidates[index]],res)
    
    combSum(index + 1,candidates,target,sum,n,arr,res)

candidates = [10,1,2,7,6,1,5]
target = 8
res = []
arr = []
combSum(0,candidates,target,0,len(candidates),arr,res)
res.sort()
print(res)