'''
Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, 
and the first element of a row is greater than the last element of the previous row (if it exists), 
and an integer target, determine if the target exists in the given mat or not.
'''

def matTarget(mat,m,n,target):
    
    for i in range(m):

        low = 0
        high = n - 1

        if matrix[i][0]<=target<=matrix[i][high]:

            while low <= high:

                mid = (low + high) // 2

                if matrix[i][mid] == target:
                    return True

                elif matrix[i][mid] < target :
                    low = mid + 1

                else:
                    high = mid - 1
                
    return False
                

matrix = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
target = 78

m = len(matrix)
n = len(matrix[0])

res = matTarget(matrix,m,n,target)
print(res)