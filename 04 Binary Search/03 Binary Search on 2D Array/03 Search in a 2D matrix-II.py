'''
Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, 
and the first element of a row is greater than the last element of the previous row (if it exists), 
and an integer target, determine if the target exists in the given mat or not.
'''

def matTarget(mat,m,n,target):
    
    row = 0
    col = n - 1
    
    while row < m and col >= 0:
        
        if matrix[row][col] == target :
            return True
        
        elif matrix[row][col] < target :
            row += 1
            
        else :
            col -= 1
    
                
    return False
                

matrix = [ [1, 2, 4], [6, 7, 8], [9, 10, 78] ]
target = 78

m = len(matrix)
n = len(matrix[0])

res = matTarget(matrix,m,n,target)
print(res)