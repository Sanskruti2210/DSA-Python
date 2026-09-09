'''
Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, 
and the first element of a row is greater than the last element of the previous row (if it exists), 
and an integer target, determine if the target exists in the given mat or not.
'''

def matTarget(mat,m,n,target):
    
    for i in range(m):

        low = 0
        high = n - 1
        
        # Check if the target is in given col
        if matrix[i][0]<=target<=matrix[i][high]:

            # Start binary search at ith row
            while low <= high:
                
                # Compute mid
                mid = (low + high) // 2

                # If target is found return 
                if matrix[i][mid] == target:
                    return True

                # If target is greater find in right half
                elif matrix[i][mid] < target :
                    low = mid + 1

                # Else find in letf half
                else:
                    high = mid - 1
                
    return False
                

matrix = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
target = 78

m = len(matrix)
n = len(matrix[0])

res = matTarget(matrix,m,n,target)
print(res)