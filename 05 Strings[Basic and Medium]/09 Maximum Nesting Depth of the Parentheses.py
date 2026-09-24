'''
A string s is a valid parentheses string (VPS) if it meets the following conditions:
It only contains digits 0-9, arithmetic operators +, -, *, /, and parentheses (, ).
The parentheses are balanced and correctly nested.
Your task is to compute the maximum nesting depth of parentheses in s. 
The nesting depth is the highest number of parentheses that are open at the same time at 
any point in the string.
'''

def maxDepth(s):
    
    # String length is 0 return 0
    if len(s) == 0:
        return 0

    # Start count from 1 as it will ignore the most outer parthesis
    count = 1
    maxCount = 0
    for par in s:
        
        # If par is ( increase count
        if par == '(':
            count += 1
            
        # Else if you find ) decrease count and update maxCount too
        elif par == ')':
            count -= 1
            maxCount = max(maxCount,count)
            
    return maxCount
        
s = "()(())((()()))"
res = maxDepth(s)
print(res)