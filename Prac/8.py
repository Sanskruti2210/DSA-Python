'''Given an N × N matrix, rotate it 90 degrees clockwise.'''

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

m = len(matrix)
n = len(matrix[0])

for i in range(m):
    
    for j in range(i + 1,n):
        
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
for row in matrix:
    
    row.reverse()
    
for i in range(m):
    
    for j in range(n):
        
        print(matrix[i][j],end = " ")
    
    print()
    
    