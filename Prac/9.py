'''Given a matrix, return its elements in spiral order.'''

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

m = len(matrix)
n = len(matrix[0])

left = 0
top = 0
right = n - 1
bottom = m - 1

ans = []

while top <= bottom and left <= right:
    
    for i in range(left,right + 1):
        ans.append(matrix[top][i])
    top += 1
        
    for j in range(top,bottom + 1):
        ans.append(matrix[j][right])
    right -= 1
        
    if top <= bottom:
        for k in range(right,left - 1,-1):
            ans.append(matrix[bottom][k])
            
    bottom -= 1
    
    if right <= left:
        for l in range(bottom,top - 1,-1):
            ans.append(matrix[l][left])
            
    left += 1
    
print(ans)