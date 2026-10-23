'''Given an m x n matrix, if an element is 0, set its entire row and column to 0.'''

matrix = [
 [1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]
]

m = len(matrix)
n = len(matrix[0])

temp = [[0 for _ in range(n)] for _ in range(m)]

for row in range(m):
    
    for col in range(n):
        
        if matrix[row][col] == 0:
            