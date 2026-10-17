'''Given an integer N, print the numbers from 1 to N using recursion.'''

def printVal(n):
    
    if n == 0:
        return
    
    printVal(n-1)
        
    print(n)
    
n = 5
printVal(n)