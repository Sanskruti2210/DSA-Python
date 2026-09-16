"""
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
You can return the intervals in any order.
"""

intervals = [[5, 7], [1, 3], [4, 6], [8, 10]]

# Sort the array first
intervals.sort()
ans = []
n = len(intervals)
i = 0

while i < n:
    
    # inialize start and end
    start = intervals[i][0]
    end = intervals[i][1]

    j = i + 1
    # If j comes in i interval then update the end
    while j < n and intervals[j][0] <= end:
        end = max(end, intervals[j][1])
        j += 1

    ans.append([start, end])

    i = j

print(ans)
