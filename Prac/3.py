'''Given an integer N, determine whether it is a Perfect Number.

A number is perfect if the sum of its proper divisors equals the number itself.'''

import math
n = 28
divisor = []

for i in range(1,math.isqrt(n) + 1):
    
    if n % i == 0:
        divisor.append(i)
        
        if i != (n // i) and (n//i) != n:
            divisor.append(n//i)
      
divisor.sort()  
print(divisor)
if sum(divisor) == n:
    print(True)
else:
    print(False)