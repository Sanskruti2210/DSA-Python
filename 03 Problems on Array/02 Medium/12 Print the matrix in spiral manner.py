"""
Given an M * N matrix, print the elements in a clockwise spiral manner.
Return an array with the elements in the order of their appearance when printed in a spiral manner.
"""

# Print Matrix in spiral manner
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
ans = []

m = len(matrix)
n = len(matrix[0])
top = left = 0
bottom = right = m - 1

while top <= bottom and left <= right:

    # left->right
    for i in range(left, right + 1):
        ans.append(matrix[top][i])
    top += 1

    # top->bottom
    for i in range(top, bottom + 1):
        ans.append(matrix[i][right])
    right -= 1

    # Check because after updating top/right,
    # there may be no row left to traverse.
    # The key idea is:
    # top <= bottom → there is still at least one row left.
    # left <= right → there is still at least one column left.
    if top <= bottom:
        # right->left
        for i in range(right, left - 1, -1):
            ans.append(matrix[bottom][i])
        bottom -= 1

    # Check because after updating bottom/right,
    # there may be no column left to traverse.
    if left <= right:
        # bottom->top
        for i in range(bottom, top - 1, -1):
            ans.append(matrix[i][left])
        left += 1

print(ans)
