"""
Given an array nums of size n which may contain duplicate elements.
return a list of pairs where each pair contains a unique element from the array and its frequency in the array.
You may return the result in any order, but each element must appear exactly once in the output.
"""

print("Enter the array first : ")
arr = list(map(int, input().split()))
print("Enter the elements whose frequency u need to find : ")
num_input = list(map(int, input().split()))

n = max(arr)
# Create a hashmap
hash = [0] * (n + 1)

for ele in arr:
    hash[ele] += 1

print("Output : ")
for ele in num_input:
    print(f"{ele} : {hash[ele]}")
