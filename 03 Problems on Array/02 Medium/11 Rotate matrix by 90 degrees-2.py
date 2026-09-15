"""
Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.
The rotation must be done in place, meaning the input 2D matrix must be modified directly.
"""

# Optimal
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

m = len(matrix)
n = len(matrix[0])


for k in matrix:
    print(k,end=' ')
    print()
print("----------------------------------------------")
# First transpose the matrix:
# swap elements across the main diagonal
for i in range(m):
    
    for j in range(i + 1, n):
        
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(f"for i = {i} j = {j}")
        for k in matrix:
            print(k,end=' ')
            print()
        print("----------------------------------------------")


# Then reverse every row
# This gives the 90° clockwise rotation.
for i in range(m):
    matrix[i].reverse()


# Example:
# Original:
# [1,2,3]
# [4,5,6]
# [7,8,9]
#
# Transpose → Reverse rows → 90° clockwise rotation

for row in matrix:
    print(row , end= ' ')
    print()
