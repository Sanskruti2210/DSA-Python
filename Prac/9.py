'''Given a string representing a positive integer, find the largest-valued odd-number substring that can be obtained by removing digits from the end.'''

s = '11251'

num = 0
max_odd = 0

for i in range(len(s)):
    
    num = num*10 + int(s[i])
    
    if num % 2 != 0:
        max_odd = max(max_odd,num)

print(max_odd)
