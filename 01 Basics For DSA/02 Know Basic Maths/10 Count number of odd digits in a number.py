'''
You are given an integer n. You need to return the number of odd digits present in the number.
The number will have no leading zeroes, except when the number is 0 itself.
'''

def numOfOdd(n):
    
    odd = 0
    
    while n > 0:
        
        # Use % to get each digit
        rmd = n % 10
        
        # Check if digit is odd
        if rmd % 2 != 0:
            odd += 1
            
        n //= 10
        
    return odd

n = 125
ans = numOfOdd(n)
print(ans)
