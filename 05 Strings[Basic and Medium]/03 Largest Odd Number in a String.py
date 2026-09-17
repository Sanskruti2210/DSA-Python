'''
Given a string s, representing a large integer, the task is to return the largest-valued odd integer 
(as a string) that is a substring of the given string s.
The number returned should not have leading zero's. But the given input string may have leading zero. 
(If no odd number is found, then return empty string.)
'''

s = "0214638"
nums = ""

n = len(s)

i = n - 1
while i >= 0:
    
    # Convert char into int
    num = int(s[i])
    
    # Check if the num is odd then break
    if num % 2 != 0 :
        break
             
    # Else continue the search
    else :
        i -= 1
   
j = 0
# Check if there is any leading zero till the index we stop our first loop  
while j <= i and s[j] != '0' :
    i += 1
        
nums = s[ j + 1 : i + 1]
print(nums)
    
    
