'''Given an array of strings, find the longest common prefix shared by all strings.'''

s = ["flower", "flow", "flight"]

s.sort()

first = s[0]
last = s[-1]

ans = ""

for i in range(min(len(first),len(last))):
    
    if first[i] != last[i]:
        break
    
    ans += first[i]
    
print(ans)
    