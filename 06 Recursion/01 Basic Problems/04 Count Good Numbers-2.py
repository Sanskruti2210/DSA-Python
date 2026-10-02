'''
A digit string is considered good if the digits at even indices (0-based) are even digits 
(0, 2, 4, 6, 8) and the digits at odd indices are prime digits (2, 3, 5, 7).
Given an integer n, return the total number of good digit strings of length n. 
As the result may be large, return it modulo 109 + 7.
A digit string is a string consisting only of the digits '0' through '9'. It may contain leading zeros.
'''

def countGoodnumber(n):
    
    # Count even and odd position
    even_position = (n + 1) // 2
    odd_position = n // 2
    Mod = 10**9 + 7
    
    return (pow(5,even_position,Mod)*pow(4,odd_position,Mod)) % Mod

n = 50
res = countGoodnumber(n)
print(res)
    