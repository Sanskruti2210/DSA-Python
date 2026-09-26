'''
Implement the power function pow(x, n) , which calculates the x raised to n i.e. xn.
Note : In output print 6 digits places after decimal point.
'''

def pow(x,n):
    
    # Positive power
    if n > 0:
        
        if n == 1:
            return x
        
        return x*pow(x,n-1)
       
    # Negative power 
    else:
        
        if n == -1:
            return 1/x
        
        return 1/x*pow(x,n+1)
    
x = 2.0000
n = -2
ans = pow(x,n)
print(f'{ans:.6f}')