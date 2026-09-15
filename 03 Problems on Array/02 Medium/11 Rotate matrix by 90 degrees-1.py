"""
Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.
The rotation must be done in place, meaning the input 2D matrix must be modified directly.
"""

# Brute Force
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

m = len(matrix)
n = len(matrix[0])

# For 90° clockwise rotation:
# columns of original matrix become rows of the new matrix
# and we traverse each column from bottom to top.
temp = [[0 for _ in range(m)] for _ in range(n)]

row_in_temp = 0

for j in range(n):
    
    col_in_temp = 0

    for i in range(m - 1, -1, -1):

        # Take elements from bottom to top
        # and place them from left to right
        temp[row_in_temp][col_in_temp] = matrix[i][j]
        col_in_temp += 1

    row_in_temp += 1


matrix = temp

for num in matrix:
    print(num,end=' ')
    print()
