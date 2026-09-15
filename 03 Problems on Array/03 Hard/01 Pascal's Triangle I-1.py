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


# Approach-1
def pascalTriangle(r, c):
    
    # Create empty array 
    triangle = []
    
    for i in range(r):
        
        # Give all col of ith row 1
        row = [1] * (i + 1)
        
        for j in range(1, i):
            
            # In pascal triangle the element is the sum of its above row 2 subsequent cols
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append it in triangle
        triangle.append(row)
        
    return triangle


for row in pascalTriangle(5,5) :
    print(row ,end = ' ')
    print()
