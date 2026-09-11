'''
Given a 2D array matrix that is row-wise sorted. 
The task is to find the median of the given matrix.
'''

import bisect

def countLessthenorEqual(row,mid):
    return bisect.bisect_right(row,mid)

def medianMatrix(matrix) : 
    
    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    while low <= high :
        
        mid = ( low + high ) // 2
        count = 0
        
        for row in matrix :
            count += countLessthenorEqual(row,mid)
            
        if count < (rows*cols + 1)//2 :
            low = mid + 1
            
        else :
            high = mid - 1
            
    return low

matrix=[ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] 
res = medianMatrix(matrix)

print(res)
