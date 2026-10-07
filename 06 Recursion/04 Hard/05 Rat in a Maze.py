'''
Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) 
and wants to reach at coordinates (n-1, n-1).
Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). 
The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).
The value 0 in grid denotes that the cell is blocked and rat cannot use that 
cell for travelling, whereas value 1 represents that rat can travel through the cell. 
If the cell (0, 0) has 0 value, then mouse cannot move to any other cell.
Note :
In a path no cell can be visited more than once.
If there is no possible path then return empty vector.
'''

def RatMace(row,col,n,x,y,grid,str,res):
    
    # Check for boundary
    if row >= x or row < 0 or col >= y or col < 0:
        return 
    
    # Check for visited
    if (row,col) in visited:
        return
    
    # Check if it can be visited or not
    if grid[row][col] == 0:
        return
    
    # Base Case
    if row == n - 1 and col == n- 1:
        res.append(str)
        return

    visited.add((row,col))
    
    # Check for all four direction
    RatMace(row + 1,col,n,x,y,grid,str + 'D',res)
    RatMace(row - 1,col,n,x,y,grid,str + 'U',res)
    RatMace(row,col + 1,n,x,y,grid,str + 'R',res)
    RatMace(row,col - 1,n,x,y,grid,str + 'L',res)
    
    visited.remove((row,col))
     
n = 3    
grid = [ [1, 0, 0] , [1, 1, 0], [0, 1, 1] ]
res = []
visited = set()
RatMace(0,0,n,len(grid),len(grid[0]),grid,"",res)

if res:
    print(res)
else:
    print(-1)