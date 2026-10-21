'''Given a string containing:
( ) [ ] { }

determine whether the brackets are properly matched and nested.'''

def isValidParthesis(s):
    
    stack = []
    
    for p in s:
        
        if p == '(' or p == '{' or p=='[':
            stack.append(p)
        elif p == ')':
            if stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif p == ']':
            if stack[-1] != '[':
                return False
            else:
                stack.pop()
        elif p == '}':
            if stack[-1] != '{':
                return False
            else:
                stack.pop()

    return True

s = "([)]"
print(isValidParthesis(s))