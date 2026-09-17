'''
Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). 
A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.
Return a string with the words in reverse order, concatenated by a single space.
'''

s = "welcome to the jungle"
result = ""

i = len(s) - 1

# init end
end = len(s) - 1

while i >= 0 :
    
    # Check for the white space
    while i >= 0 and s[i] == ' ':
        i -= 1
        
    end = i
    
    # Skip white spaces
    while i >= 0 and s[i] != ' ':
        i -= 1
        
    # add the word into final result
    result += s[ i + 1 : end + 1 ] + ' '
    
    i -= 1

print(result.strip())
    
    