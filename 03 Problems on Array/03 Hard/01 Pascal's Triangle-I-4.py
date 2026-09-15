"""
Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.
In Pascal's triangle:
The first row contains a single element 1.
Each row has one more element than the previous row.
Every row starts and ends with 1.
For all interior elements (i.e., not at the ends), the value at position (r, c) is
computed as the sum of the two elements directly above it from the previous row:
Pascal[r][c]=Pascal[r-1][c-1]+Pascal[r-1][c]
where indexing is 1-based
"""


# Approach-4
def FindRow(r, c):
    
    n = r - 1
    k = c - 1
    
    result = 1
    
    for i in range(k):
        result *= n - i
        result //= i + 1

    print(result)


FindRow(5, 3)
