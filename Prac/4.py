'''Given two strings s and t, determine whether they are isomorphic.

Two strings are isomorphic if characters in s can be mapped to characters in t such that the mapping is one-to-one and preserves the character pattern.'''

def isomorphic(s,t):
    
    if len(s) != len(t):
        return False
    
    map1 = {}
    map2 = {}
    
    for i in range(len(s)):
        
        if s[i] in map1:
            
            if map1[s[i]] != t[i]:
                return False
            
        if t[i] in map2:
            
            if map2[t[i]] != s[i]:
                return False
            
        map1[s[i]] = t[i]
        map2[t[i]] = s[i]
            
    return True
        
s = "egg"
t = "add"

res = isomorphic(s,t)
print(res)