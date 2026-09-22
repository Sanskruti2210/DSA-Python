'''
Given two strings s and t, determine if they are isomorphic. 
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the 
order of characters. No two characters may map to the same character, but a character may map to itself.
'''

def isomorphic(s,t):
    if len(s) != len(t) :
        return False

    map1 = {}
    map2 = {}
    
    for i in range(len(s)):
        
        # s[i] is already in mapping
        if s[i] in map1:
            if map1[s[i]] != t[i]:
                return False
            
        # t[i] already belongs to another character 
        if t[i] in map2:
            if map2[t[i]] != s[i]:
                return False
        
        map1[s[i]] = t[i]
        map2[t[i]] = s[i]
        
    return True
    
s = "paper" 
t = "title"
result  = isomorphic(s,t)
print(result)