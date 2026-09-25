'''
Given a string s, return the longest palindromic substring in s.
A palindromic substring is a contiguous sequence of characters within the string that reads 
the same forward and backward.
'''

def palindromicString(s):
    
    if len(s) == 0:
        return 0
    
    res = ""
    
    for i in range(len(s)):
        
        # Odd length
        left = i
        right = i
        
        while left >=0 and right < len(s) and s[left]==s[right]:
            
            # Store longest palindrome
            if right - left + 1 > len(res):
                res = s[left : right + 1]
                
            left -= 1
            right += 1
            
        # Even length
        left = i
        right = i + 1
        
        while left >=0 and right < len(s) and s[left]==s[right]:
            
            # Store the longest palindrome
            if right - left + 1 > len(res):
                res = s[left : right + 1]
                
            left -= 1
            right += 1
        
    return res
        
s = "cbbd"
ans = palindromicString(s)
print(ans)