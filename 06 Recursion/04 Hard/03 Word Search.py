'''
Given a grid of n x m dimension grid of characters board and a string word.The word can 
be created by assembling the letters of successively surrounding cells, whether they are next to 
each other vertically or horizontally. 
It is forbidden to use the same letter cell more than once.
Return true if the word exists in the grid otherwise false.
'''

def wordSearch(index,row,col,m,n,board,word,l):
    
    if index == l:
        return True
    
    if row < 0 or row >= n or col < 0 or col >= m:
        return  False
    
    if board[row][col] != word[index]:
        return False
            
    temp = board[row][col]
    board[row][col] = '#'
            
    if (wordSearch(index + 1,row - 1,col,m,n,board,word,l) or 
        wordSearch(index + 1,row + 1,col,m,n,board,word,l) or
        wordSearch(index + 1,row,col + 1,m,n,board,word,l) or 
        wordSearch(index + 1,row,col - 1,m,n,board,word,l)):
        return True
    
    board[row][col] = temp
    
    return False

def exist(board,word):
    
    n = len(board)
    m = len(board[0])
    l = len(word)
    
    for r in range(n):
        
        for c in range(m):
            
            if wordSearch(0,r,c,m,n,board,word,l):
                return True
            
    return False

board = [ ["A", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "D", "E", "E"] ] 
word = "ABCB"
res = exist(board,word)
print(res)