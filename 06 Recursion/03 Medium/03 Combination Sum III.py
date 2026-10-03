'''
Determine all possible set of k numbers that can be added together to equal 
n while meeting the following requirements:
There is only use of numerals 1 through 9.
A single use is made of each number.
Return list of every feasible combination that is allowed. 
The combinations can be returned in any order, but the list cannot have 
the same combination twice.
'''

def combSum3(num,n,k,arr,sum,res):
    
    # Base Case
    if len(arr) == k:
        
        if sum == n:
            res.append(arr)
        return
    
    # num can go max till 10
    if num == n or num == 10:
        return
    
    # Pick
    combSum3(num + 1,n,k,arr + [num],sum + num,res)
    
    # Not Pick
    combSum3(num + 1,n,k,arr,sum,res)
    
arr = []
res = []
k = 3
n = 8
combSum3(1,n,k,arr,0,res)
print(res)