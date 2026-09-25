'''
You are given an integer n. You need to check if the number is a perfect number or not. 
Return true if it is a perfect number, otherwise, return false.
A perfect number is a number whose proper divisors (excluding the number itself) add up to 
the number itself.
'''

import math

def isPerfect(n):
    
    divsior = []
    
    # Check till sqrt of n
    for i in range(1,int(math.sqrt(n)) + 1):
        
        # If n is divisible by i
        if n % i == 0:
            divsior.append(i)
            
            # Store only proper divisor
            if i != (n//i) and (n//i) != n:
                divsior.append(n//i)
                
    if n == sum(divsior):
        return True
    
    else :
        return False
    
n = 28
ans = isPerfect(n)
print(ans)