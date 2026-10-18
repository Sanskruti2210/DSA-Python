'''Given an integer N, find the number of prime numbers in the range:'''

import math

def isPrime(n):
    
    if n > 1:
        
        for i in range(2,math.isqrt(n) + 1):
            
            if n % i == 0:
                return False

        return True 

def countPrime(n):
    
    count = 0
    
    for i in range(1,n + 1):
    
        if isPrime(i):
            count += 1
    
    return count

n = 10
print(countPrime(n))