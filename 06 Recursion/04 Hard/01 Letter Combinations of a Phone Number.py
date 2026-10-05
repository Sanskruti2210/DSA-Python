'''
Given a string consisting of digits from 2 to 9 (inclusive). 
Return all possible letter combinations that the number can represent.
Mapping of digits to letters is given in first example.
'''

def letterComb(index,digits,n,letters,str,res):
    
    # Edge Case
    if digits == "":
        return []
    
    # Base Case
    if index == n:
        res.append(str)
        return
    
    # Check for every combination
    for ch in letters[digits[index]]:
        new_str = str + ch
        letterComb(index + 1,digits,n,letters,new_str,res)
     
letters = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz'    
}
digits = "8"
res = []
str = ""
n = len(digits)
letterComb(0,digits,n,letters,str,res)
print(res)