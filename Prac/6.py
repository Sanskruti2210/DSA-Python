'''Given a valid parentheses string, remove the outermost pair of parentheses from every primitive valid parentheses substring.'''

s = "(()())(())"

ans = ""

level = 0
    
for i in range(len(s)):
    
    if s[i] == "(":
        
        if level > 0:
            ans += s[i]
        
        level += 1
        
        
    elif s[i] == ')':
        
        level -= 1
        
        if level > 0 :
            ans += s[i]
        
print(ans)
        