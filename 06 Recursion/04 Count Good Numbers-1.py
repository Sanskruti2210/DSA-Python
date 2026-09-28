'''
A digit string is considered good if the digits at even indices (0-based) are even digits 
(0, 2, 4, 6, 8) and the digits at odd indices are prime digits (2, 3, 5, 7).
Given an integer n, return the total number of good digit strings of length n. 
As the result may be large, return it modulo 109 + 7.
A digit string is a string consisting only of the digits '0' through '9'. It may contain leading zeros.
'''

def countGoodnumber(n):
    
    count = 0
    
    def genrateString(index):
        
        nonlocal count
        
        # Increase count if we check as posibility
        if index == n:
            count += 1
            return
        
        # even index
        if index % 2 == 0:
            choices = [0,2,4,6,8]
            
        # odd index
        else:
            choices = [2,3,5,7]
            
        for digit in choices:
            genrateString(index + 1)
            
    genrateString(0)
    
    return count

n = 5
res = countGoodnumber(n)
print(res)
    