'''
The challenge of arranging n queens on a n x n chessboard so that no two 
queens attack one another is known as the "n-queens puzzle."
Return every unique solution to the n-queens puzzle given an integer n. 
The answer can be returned in any sequence.
Every solution has a unique board arrangement for the placement of the n-queens,
where 'Q' and '.' stand for a queen and an empty space, respectively.
Here are the attack rules for N-Queens:
1.Same Row - No two queens can be in the same row.
2.Same Column - No two queens can be in the same column.
3.Same Diagonal (top-left to bottom-right) - No two queens can share the same diagonal 
where (row - col) is equal.
4.Same Anti-Diagonal (top-right to bottom-left) - No two queens can share the same 
anti-diagonal where (row + col) is equal.
'''

def nQueens(row,n,board,res):
    
    if row == n :
        res.append(["".join(r) for r in board])
        return

    
    for col in range(n):
        
        if col in cols:
            continue
        
        if row - col in diag:
            continue
        
        if row + col in anti_diag:
            continue
        
        board[row][col] = 'Q'
        cols.add(col)
        diag.add(row - col)
        anti_diag.add(row + col)
        
        nQueens(row + 1, n, board, res)
        
        board[row][col] = '.'
        cols.remove(col)
        diag.remove(row - col)
        anti_diag.remove(row + col)
     
  
n = 4   
board = [['.' for _ in range(n)] for _ in range(n)]
res = []
cols = set()
diag = set()
anti_diag = set()
nQueens(0,n,board,res)
print(res)
            


