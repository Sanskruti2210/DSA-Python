"""
Given an array arr of n elements.
The task is to reverse the given array in-place using recursion.
"""

def reverse(left, right, arr):

    # Example:
    # arr = [1, 2, 3, 4, 5]
    #
    # left = 0, right = 4
    #
    # Step 1:
    # Swap arr[0] and arr[4]
    # [5, 2, 3, 4, 1]
    #
    # Step 2:
    # left = 1, right = 3
    # Swap arr[1] and arr[3]
    # [5, 4, 3, 2, 1]
    #
    # Step 3:
    # left = 2, right = 2
    #
    # left >= right
    # Base case reached, so stop recursion.

    # Base case:
    # When both pointers meet or cross each other,
    # the array has been completely reversed.
    if left >= right:
        return

    # Swap elements at left and right indexes
    arr[left], arr[right] = arr[right], arr[left]

    # Move left forward and right backward
    reverse(left + 1, right - 1, arr)


arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

reverse(left, right, arr)

print(arr)
