'''
Given a string s partition string s such that every substring of partition is palindrome. 
Return all possible palindrome partition of string s.
'''

def palindromePartition(index,s,n,arr,res):
    
    # Base Case
    if index == n :
        res.append(arr[:])
        return
    
    # Check for substrings
    for i in range(index,n):
        
        sub = s[index : i + 1]
        
        if sub == sub[::-1]:
            
            arr.append(sub)
            
            palindromePartition(i + 1,s,n,arr,res)
            
            arr.pop()            
    
s = "ab"
res = []
n = len(s)
palindromePartition(0,s,n,[],res)
print(res)
    
