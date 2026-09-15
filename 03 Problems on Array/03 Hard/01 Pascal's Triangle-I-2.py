"""
Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.
In Pascal's triangle:
The first row contains a single element 1.
Each row has one more element than the previous row.
Every row starts and ends with 1.
For all interior elements (i.e., not at the ends), the value at position (r, c) is
computed as the sum of the two elements directly above it from the previous row:
Pascal[r][c]=Pascal[r−1][c−1]+Pascal[r−1][c]
where indexing is 1-based
"""


# Approach-2
def Factorial(n):
    
    fact = 1
    
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


def pascalPrint(row):
    for i in range(row):
        for j in range(i + 1):
            print(Factorial(i) // (Factorial(j) * Factorial(i - j)), end=" ")
        print()


pascalPrint(5)
