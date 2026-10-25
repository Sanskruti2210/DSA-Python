'''Given a valid parentheses string, find its maximum nesting depth.'''

s = "(1+(2*3)+((8)/4))+1"

level = 0
max_depth = 0

for i in range(len(s)):
    
    if s[i] == "(":
        
        level += 1
        
    elif s[i] == ")":
        
        level -= 1
        
    max_depth = max(max_depth,level)
    
print(max_depth)