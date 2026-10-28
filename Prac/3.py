'''Given an integer array and a target, find all unique quadruplets whose sum equals the target.'''

nums = [1,0,-1,0,-2,2]
target = 0

n = len(nums)

# Method - 1
# ans = set()

# for i in range(n):

#     hashmap = set()
#     for j in range(i + 1,n):

#         for k in range(j + 1,n):

#             for l in range(k + 1,n):

#                 if nums[i] + nums[j] + nums[k] + nums[l] == target:

#                     qudraplet = tuple(sorted([nums[i],nums[j],nums[k],nums[l]]))

#                     if qudraplet not in hashmap:

#                         ans.add(qudraplet)

#                     hashmap.add(qudraplet)

# for item in ans:
#     print(list(item))

# Method - 2
# ans1 = set()
# for i in range(n):

#     hashmap = set()

#     for j in range(i + 1,n):

#         for k in range(j + 1,n):

#             fourth = target - (nums[i] + nums[j] + nums[k])

#             if fourth in hashmap:
#                 qudraplet = tuple(sorted([nums[i],nums[j],nums[k],fourth]))
#                 ans1.add(qudraplet)

#             hashmap.add(nums[k])

# for item in ans1:
#     print(list(item))

# Method 3

ans2 = []
nums.sort()

for i in range(n):

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1,n):

        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        left = j + 1
        right = n - 1

        while left < right:

            total = nums[i] + nums[j] + nums[left] + nums[right]

            if total == target:
                ans2.append([nums[i],nums[j],nums[left],nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < target:
                left += 1

            else:
                right -= 1

for item in ans2:

    print(list(item))


