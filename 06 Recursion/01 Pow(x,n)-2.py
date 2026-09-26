'''
Implement the power function pow(x, n) , which calculates the x raised to n i.e. xn.
Note : In output print 6 digits places after decimal point.
'''

def pow(x,n):
    
    # Base case
    if n == 0:
        return 1
    
    # n is negative make x = 1 / x
    if n < 0:
        
        x = 1 / x
        # make positive so we only have to deal with positive power
        n = -n
        
    # Use binary expontation as 2^10 = 2^5 * 2^5
    half = pow(x,n//2)
    
    # For even power
    if n % 2 == 0:
        return half*half
    
    # For odd we need to mul extra x 
    # For example : 2^5 = 2 * 2^2 * 2^2
    else:
        return x*half*half
    
x = 2.0000
n = 10
ans = pow(x,n)
print(f'{ans:.6f}')
    
    