'''
You are given an integer n. You need to find out the number of prime numbers in the range [1, n] 
(inclusive). Return the number of prime numbers in the range.
A prime number is a number which has no divisors except, 1 and itself.
'''

import math

def primeTillN(n):
    
    # init count
    count = 0
    
    for num in range(2,n + 1):
        
        is_prime = True
        
        for divisor in range(2,int(math.sqrt(num)) + 1):
            
            if num % divisor == 0:
                is_prime = False
                break
            
        if is_prime:
            count += 1
                
    return count

n = 10
ans = primeTillN(n)
print(ans)