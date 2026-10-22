'''Given an integer N, print all of its divisors.'''

import math
n = 36
divisor = []

for i in range(1,math.isqrt(n) + 1):
    
    if n % i == 0:
        divisor.append(i)
        
        if i != (n // i):
            divisor.append(n//i)
      
divisor.sort()  
print(divisor)