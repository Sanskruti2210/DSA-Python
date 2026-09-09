'''
Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order, 
find the index of the row with the maximum number of ones.
If two rows have the same number of ones, consider the one with a smaller index. 
If no 1 exists in the matrix, return -1.
'''

def maxRowWith1s(mat,m,n):
    
    ans = - 1
    max1s = 0
    
    # Start traversing in matrix
    for i in range(m):
        
        low = 0
        high = n - 1
        
        # Start binary search 
        while low <= high:
            
            mid = ( low + high ) // 2
            
            # If we find one then to check if it is 1s one check on 
            # left half as matrix is in asecnding order
            if mat[i][mid] == 1:
                high = mid - 1
                
            # Else check on right half
            else:
                low = mid + 1
              
        # Low with be at index where first 1 is found  
        total1s = n - low
            
        # Update the max1s
        if total1s > max1s:
            max1s = total1s
            ans = i
                
    return ans
            

mat = [ [0, 0], [0, 0] ]
m = len(mat)
n = len(mat[0])

res = maxRowWith1s(mat,m,n)
print(res)
