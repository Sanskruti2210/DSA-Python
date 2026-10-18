'''Roman numerals use these symbols:
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900'''

s = "MCMXCIV"
count = 0
i = 0

n = len(s) - 1

while i < len(s):
    
    if s[i] == "I":
        if i != n and s[i + 1] == "V":
            count += 4
            i += 2
        elif i != n and s[i + 1] == "X":
            count += 9
            i += 2
        else:
            count += 1
            i += 1
            
    elif s[i] == "V":
        count += 5
        i += 1
      
    elif s[i] == "X":
        if i != n and s[i + 1] == "L":
            count += 40
            i += 2
        elif i != n and s[i + 1] == "C":
            count += 90
            i += 2
        else:
            count += 10  
            i += 1
    
    elif s[i] == "L":
        count += 50
        i += 1
        
    elif s[i] == "C":
        if i != n and s[i + 1] == "D":
            count += 400
            i += 2
        elif i != n and s[i + 1] == "M":
            count += 900
            i += 2
        else:
            count += 100
            i += 1
            
    elif s[i] == "D":
        count += 500
        i += 1
        
    elif s[i] == "M":
        count += 1000  
        i += 1
        
print(count)