'''Given an array containing positive and negative integers, rearrange the elements so that positive and negative numbers appear alternately.'''

nums = [3, 1, -2, -5, 2, -4]
ans = [0]*len(nums)
pos_index = 0
neg_index = 1

for i in range(len(nums)):
    
    if nums[i] > 0:
        ans[pos_index] = nums[i]
        pos_index += 2
    else:
        ans[neg_index] = nums[i]
        neg_index += 2
        
print(ans)