"""
Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
Merge both the arrays into a single array sorted in non-decreasing order.
The final sorted array should be stored inside the array nums1 and it should be done in-place.
nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
nums2 has a length of n.
"""

nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]

m = 4
n = 3
k = m + n - 1

left = m - 1
right = n - 1

while left >= 0 and right >= 0:
    if nums1[left] < nums2[right]:
        nums1[k] = nums2[right]
        right -= 1
    else:
        nums1[k] = nums1[left]
        left -= 1
    k -= 1

while right >= 0:
    nums1[k] = nums2[right]
    right -= 1
    k -= 1

print(nums1)
