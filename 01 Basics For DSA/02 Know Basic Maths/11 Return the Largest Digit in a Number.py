'''
You are given an integer n. Return the largest digit present in the number.
'''

def largestDigit(n):
    
    digits = []
    
    while n > 0 :
        
        # Use reminder to get each digit
        rmd = n % 10
        digits.append(rmd)
        n //= 10
      
    # return max of digits  
    return max(digits)

n = 99
ans = largestDigit(n)
print(ans)
