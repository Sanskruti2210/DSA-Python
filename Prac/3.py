nums = [1, 2, 3, 4, 5]

ans = [0]*len(nums)

n = len(nums)
m = n - 1

for i in range(len(nums)):
    
    ans[m] = nums[i]
    m -= 1
    
print(ans)