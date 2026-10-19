'''Given an integer array, count how many elements are even.'''

even = 0

nums = [1, 2, 4, 7, 8, 9]

for num in nums:
    
    if num % 2 == 0:
        even += 1
        
print(even)