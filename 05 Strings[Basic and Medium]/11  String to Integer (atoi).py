'''
Implement the function myAtoi(s) which converts the given string s to a 32-bit 
signed integer (similar to the C/C++ atoi function).
Steps to Implement:
First, ignore any leading whitespace characters ' ' until the first non-whitespace character is found.
Check the next character to determine the sign. If it's a '-', the number should 
be negative. If it's a '+', the number should be positive. If neither is found, assume the number is positive.
Read the digits and convert them into a number. Stop reading once a non-digit 
character is encountered or the end of the string is reached. Leading zeros should be ignored during conversion.
The result should be clamped within the 32-bit signed integer range: 
[-2147483648, 2147483647]. If the computed number is outside this range, 
return -2147483648 if the number is less than -2147483648, or return 2147483647 
if the number is greater than 2147483647.
Finally, return the computed number after applying all the above steps.
'''

def atoi(s):
    
    if len(s) == 0:
        return 0
    
    num = 0
    sign = 1
    n = len(s)
    
    i = 0
        
    while i < n and s[i] == ' ':
        i += 1
        
    if s[i] == '-':
        sign = -1
        i += 1
        
    elif s[i] == '+':
        i += 1
        
    while i < n and '0' <= s[i] <= '9':
        num = num*10 + int(s[i])
        i += 1
        
    if num < -2147483648:
        return -2147483648
    elif num > 2147483647:
        return 2147483647
    
    return num

s = "with words 4193"
res = atoi(s)
print(res)