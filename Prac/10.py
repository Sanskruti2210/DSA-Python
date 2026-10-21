'''Given a string s, find the length of the longest substring without repeating characters.'''

s = "abcabcbb"

ans = []
start = 0
length = 0
max_length = 0

for ch in range(len(s)):
    
    if s[ch] not in ans:
        ans.append(s[ch])
    else:
        length = ch - start
        start = ch
        max_length = max(max_length,length)
        ans = []
        
print(max_length)
    
    