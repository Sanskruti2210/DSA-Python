'''Given an integer array, find all unique triplets [a,b,c] such that:'''

nums = [-1, 0, 1, 2, -1, -4]

# ans = set()

# for i in range(len(nums)):
    
#     hash = []
    
#     for j in range(i + 1,len(nums)):
        
#         for k in range(j + 1,len(nums)):
            
#             if nums[i] + nums[j] + nums[k] == 0:
                
#                 pair = tuple(sorted([nums[i],nums[j],nums[k]]))
                
#                 if pair not in hash:
                    
#                     ans.add(pair)
                    
#                 hash.append(pair)
                
# for item in ans:
#     print(list(item))
    
# Method - 2
# ans2 = set()
# for i in range(len(nums)):
    
#     hashmap = set()
    
#     for j in range(i + 1,len(nums)):
        
#         third = - (nums[i] + nums[j])
        
#         if third in hashmap:
#             triplet = tuple(sorted([nums[i],nums[j],third]))
#             ans2.add(triplet)
            
#         hashmap.add(nums[j])
        
# for item in ans2:
    
#     print(list(item))

# Method - 3
ans3 = []
n = len(nums)
nums.sort()
for i in range(len(nums)):

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:

        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            ans3.append([nums[i],nums[left],nums[right]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1


        elif total < 0:
            left += 1

        else:
            right -= 1

print(ans3)
for item in ans3:
    print(list(item))