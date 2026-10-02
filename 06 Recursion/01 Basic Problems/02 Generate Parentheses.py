'''
Given an integer n.Generate all possible combinations of well-formed parentheses of length 2 x N.
'''

def generateParthesis(n):
    
    res = []
    
    def backTrack(s,open,close):
        
        if open == n and close == n:
            res.append(s)
            return
            
        if open < n :
            backTrack(s + '(',open + 1,close)
            
        if close < open :
            backTrack(s + ')',open,close + 1)
            
    backTrack("",0,0)
    
    return res
    
n = 4
ans = generateParthesis(n)
print(ans)