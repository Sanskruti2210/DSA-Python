'''
Roman numerals are represented by seven different symbols:

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
Roman numerals are typically written from largest to smallest, left to right. However, in specific cases,
a smaller numeral placed before a larger one indicates subtraction.
The following subtractive combinations are valid:
I before V (5) and X (10) → 4 and 9
X before L (50) and C (100) → 40 and 90
C before D (500) and M (1000) → 400 and 900
Given a Roman numeral, convert it to an integer.
'''

def romanToint(s):
    
    res = 0
    
    i = 0
    
    while i < len(s):
        
        if s[i] == 'I':
            
            if i + 1 < len(s) and s[i + 1] == 'V':
                res += 4
                i += 1
                
            elif i + 1 < len(s) and s[i + 1] == 'X':
                res += 9
                i+= 1
                
            else :
                res += 1
            
        elif s[i] == 'V':
            res += 5
            
        elif s[i] == 'X':
            
            if i + 1 < len(s) and s[i + 1] == 'L':
                res += 40
                i += 1
                            
            elif i + 1 < len(s) - 1 and s[i + 1] == 'C':
                res += 90
                i+= 1
                            
            else :
                res += 10
            
        elif s[i] == 'L':
            res += 50
                    
        elif s[i] == 'C':
            
            if i + 1 < len(s) - 1 and s[i + 1] == 'D':
                res += 400
                i += 1
                                        
            elif i + 1 < len(s) - 1 and s[i + 1] == 'M':
                res += 900
                i+= 1
                                        
            else :
                res += 100
            
        elif s[i] == 'D':
            res += 500
                    
        elif s[i] == 'M':
            res += 1000
            
        i += 1
        
    return res
            
s = "XLII"
result = romanToint(s)
print(result)


