'''
Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, 
and the first element of a row is greater than the last element of the previous row (if it exists), 
and an integer target, determine if the target exists in the given mat or not.
'''

# In this approach we take array as 1D array and according to that we do normal binary search
def matTarget(mat,m,n,target):
    
    low = 0
    high = m*n - 1
    
    # Start binary search
    while low <= high:
        
        # Compute mid
        mid = ( low + high ) // 2
        
        # Compute row and col
        row = mid // n
        col = mid % n
        
        # If target is found return True
        if matrix[row][col] == target:
            return True
        
        # Else if target is greater find in right half
        elif matrix[row][col] < target :
            low = mid + 1
          
        # Else fing in letf half  
        else :
            high = mid - 1
                
    return False
                

matrix = [ [1, 2, 4], [6, 7, 8], [9, 10, 78] ]
target = 78

m = len(matrix)
n = len(matrix[0])

res = matTarget(matrix,m,n,target)
print(res)