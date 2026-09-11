'''
Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] 
and return the array [i, j].A peak element in a 2D grid is an element that is strictly greater than all of its 
adjacent neighbours to the left, right, top, and bottom.
Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
Note: As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.
'''

def findPeak(mat,m,n):
    
    low = 0 
    high = n - 1
    
    while low <= high:
        
        mid = (low + high) // 2
        
        
        max_col = mat[0][mid]
        row_index = 0
        
        for i in range(m):
            
            if mat[i][mid] > max_col :
                max_col = mat[i][mid]
                row_index = i
        
        left = mat[row_index][mid - 1] if mid - 1 >= 0 else float('-inf')
        right = mat[row_index][mid + 1] if mid + 1 < n else float('-inf')
        
        if max_col > left and max_col > right :
            return [row_index,mid]
        elif max_col < left :
            high = mid - 1
        elif max_col < right :
            low = mid + 1 
          
    return -1  

mat = [
    [10,  8, 10,  9,  7,  6,  5],
    [12, 11,  9, 13,  8,  7,  4],
    [14, 15,  7,  6, 16,  5,  3],
    [13,  9,  8,  7, 17,  4,  2],
    [11, 10,  6,  5,  9,  3,  1],
    [ 8,  7,  4,  2,  1,  0, -1]
]
m = len(mat)
n = len(mat[0])

res = findPeak(mat,m,n)
print(res)