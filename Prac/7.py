'''Given an m x n matrix, if an element is 0, set its entire row and column to 0.'''

# Method-1
matrix = [
 [1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]
]

m = len(matrix)
n = len(matrix[0])

# for row in range(m):
    
#     for col in range(n):
        
#         if matrix[row][col] == 0:
            
#             for i in range(n):
#                 if matrix[row][i] != 0:
#                     matrix[row][i] = -1
                
#             for j in range(m):
#                 if matrix[j][col] != 0 :
#                     matrix[j][col] = -1
                
# for i in range(m):
    
#     for j in range(n):
        
#         if matrix[i][j] == -1:
#             matrix[i][j] = 0
        
# for row in matrix:
    
#     for col in row:
        
#         print(col,end= " ")
        
#     print()
    
# Method - 2 

# row = [0]*m
# col = [0]*n

# for i in range(m):
    
#     for j in range(n):
        
#         if matrix[i][j] == 0:
#             row[i] = 1
#             col[j] = 1
            
# for i in range(m):
    
#     for j in range(n):
        
#         if row[i] or col[j]:
#             matrix[i][j] = 0
        
            
# print(row,col)
            
# for row in matrix:
    
#     for col in row:
        
#         print(col,end= " ")
        
#     print()
    
# Method - 3

col0 = 1

for i in range(m):
    
    for j in range(n):
        
        if matrix[i][j] == 0:
            
            matrix[i][0] = 0
            if j !=0 :
                matrix[0][j] = 0
            else:
                col0 = 0
            
for i in range(1,m):
    
    for j in range(1,n):
        
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            
            matrix[i][j] = 0
            
if col0 == 0:
    
    for i in range(m):
        
        matrix[i][0] = 0

if matrix[0][0] == 0:
    
    for j in range(n):
        
        matrix[0][j] = 0
        
for row in matrix:
    
    for col in row:
        
        print(col,end= " ")
        
    print()
        