'''Implement conversion of a string into a 32-bit signed integer.

The string may contain:
- leading spaces
- an optional + or -
- digits
- characters after the number'''

s = "1728abc"
ans = 0
sign = 1

i = 0

while i < len(s):
    
    while i < len(s) and s[i] == " ":
        i += 1
        
    if s[i] == "-":
        sign = -1
        i += 1
    elif s[i] == "+":
        i += 1
        
    while i < len(s) and s[i] >= "0" and s[i] <= "9":
        ans = ans*10 + int(s[i])
        i += 1
        
    i += 1
    
ans = ans*sign
print(ans)