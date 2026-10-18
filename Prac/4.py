'''Given two integers r and c, return the value at the r-th row and c-th column of Pascal's Triangle.
Both r and c are 1-indexed.'''

def pasCalRow(r,c):
    
    val = 1
    for i in range(1,c):
        val = val*(r - i) // i
        
    return val

print(pasCalRow(5,3))
    

