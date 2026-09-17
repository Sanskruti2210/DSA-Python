'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

str = ["flowers" , "flow" , "fly", "flight" ]
ans = ""

# Sort the string
str.sort()

# Store first string 
first = str[0]

# Store last string
last = str[-1]
    
print(str)
for i in range(min(len(first),len(last))):
    
    # Char differs break
    if first[i] != last[i] :
        break
    
    # Add char into ans 
    ans += first[i]
    
print(ans)
    
    