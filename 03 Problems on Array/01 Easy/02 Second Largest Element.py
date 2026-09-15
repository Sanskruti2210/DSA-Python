"""
Given an array of integers nums, return
the second-largest element in the array.
If the second-largest element does not exist, return -1.
"""

"""
Given an array of integers nums, return the value of the largest element in the array
"""

nums = [1, 5, 42 ,67 ]
max1 = float("-inf")
max2 = float("-inf")

for i in range(len(nums)):

    # If current num is greater than max1 then max2 would be max1 and then update max1
    # For Example : initially max1 = 1 after that nums[i] = 5 max1 = 5 but as max1 is updated
    # and we found more greater element we should replace max2 with max1
    # Think it like 5 2 1 now new num is 8 so it would be 8 5 2 1 so now max2 = previous max1 and max1 = new num
    if nums[i] > max1:
        max2 = max1
        max1 = nums[i]
    elif nums[i] > max2:
        max2 = nums[i]

print(max2)
