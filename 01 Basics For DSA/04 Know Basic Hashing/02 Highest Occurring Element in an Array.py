"""
Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times.
If there are multiple elements that appear a maximum number of times, find the smallest of them.
Please note that this section might seem a bit difficult without prior knowledge on what hashing is,
we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to
give a shot to the problem. Cheers!
"""

print("Enter the array first : ")
arr = list(map(int, input().split()))
max_val = max(arr)

# Create a hashmap
hash = [0] * (max_val + 1)

for ele in arr:
    hash[ele] += 1

ans = max(hash)
print("Highest Freq : ", hash.index(ans))
