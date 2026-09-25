'''
The beauty of a string is defined as the difference between the frequency of the most frequent 
character and the least frequent character (excluding characters that do not appear) in that string.
Given a string s, return the sum of beauty values of all possible substrings of s.
'''

def sumOfBeauty(s):
    
    if len(s) == 0:
        return 0
    
    total = 0
    max_freq = 0
    min_freq = 0
    
    for i in range(len(s)):
        
        freq = {}
        
        for j in range(i,len(s)):
            
            # Add the current character freq
            freq[s[j]] = freq.get(s[j],0) + 1
            
            # Compute max and min freq values
            max_freq = max(freq.values()) 
            min_freq = min(freq.values())
            
            beauty = max_freq - min_freq
            
            total += beauty
            
    return total

s = "aabcbaa"
ans = sumOfBeauty(s)
print(ans)
            
            
        
        