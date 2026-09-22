'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

def isAnagram(s,t):
    if len(s) != len(t):
        return False

    stringS = list(s).sort()
    stringT = list(t).sort()
    
    if stringS == stringT:
        return True
    
    return False
    
s = "anagram" 
t = "nagaram"

result = isAnagram(s,t)
print(result)