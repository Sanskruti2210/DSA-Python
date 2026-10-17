'''Given two strings s and t, determine whether they are anagrams of each other.
Two strings are anagrams if they contain the same characters with the same frequencies.'''

s = "anagram"
t = "nagaram"

count1 = {}

for ch in s:
    
    count1[ch] = count1.get(ch,0) + 1
   
count2 = {} 

for ch in t:
    count2[ch] = count2.get(ch,0) + 1
    
if count1 == count2:
    print(True)
else:
    print(False)