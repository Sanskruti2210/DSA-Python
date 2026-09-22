'''
You are given a string s. 
Return the array of unique characters, sorted by highest to lowest occurring characters.
If two or more characters have same frequency then arrange them in alphabetic order.
'''

def sortByFreq(s):
    
    count = {}
    
    for ch in s:
        count[ch] = count.get(ch,0) + 1
        
    result = list(sorted(count,key = lambda ch : (count[ch],ch),reverse=True))
    
    return result

s = "tree"
result = sortByFreq(s)
print(result)