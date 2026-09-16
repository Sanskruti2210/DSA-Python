'''
A valid parentheses string is defined by the following rules:
    It is the empty string "".
    If A is a valid parentheses string, then so is "(" + A + ")".
    If A and B are valid parentheses strings, then A + B is also valid.
A primitive valid parentheses string is a non-empty valid string that cannot 
be split into two or more non-empty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: 
s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in the 
primitive decomposition of s.
'''

string = "()(()())(())"

# init empty string
result = ""

# init level to check whatever we are inside the () or not
level = 0

for char in string :

    if char == '(':
        
        # Check if we are inside parthesis or not
        if level > 0:
            result += char
            
        # increase the nesting level for '('
        level += 1
    
    elif char == ')':
        
        # Decrease the nesting level for '('
        level -= 1
        
        # Check if we are inside parthesis or not
        if level > 0:
            result += char
            
print(result)

            
            
