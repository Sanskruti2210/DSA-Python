'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

def isAnagram(s,t):
    
    if len(s) != len(t):
        return False

    count = {}
    
    for ch in s:
        count[ch] = count.get(ch,0) + 1
        
    for ch in t:
        if ch not in count:
            return False
        
        count[ch] -= 1
        
        if count[ch] < 0:
            return False
    
    return True
    
s = "anagram" 
t = "nagaram"

result = isAnagram(s,t)
print(result)