'''
Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, 
and the first element of a row is greater than the last element of the previous row (if it exists), 
and an integer target, determine if the target exists in the given mat or not.
'''

def matTarget(mat,m,n,target):
    
    low = 0
    high = m*n - 1
    
    while low <= high:
        
        mid = ( low + high ) // 2
        
        row = mid // n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        
        elif matrix[row][col] < target :
            low = mid + 1
            
        else :
            high = mid - 1
                
    return False
                

matrix = [ [1, 2, 4], [6, 7, 8], [9, 10, 78] ]
target = 78

m = len(matrix)
n = len(matrix[0])

res = matTarget(matrix,m,n,target)
print(res)