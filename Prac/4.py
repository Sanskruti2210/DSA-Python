'''Given an integer array containing positive, negative, and zero values, find the length of the longest subarray whose sum is 0.'''

nums = [15,-2,2,-8,1,7,10,23]

n = len(nums)
prefix = {}
current_sum = 0
max_len = 0

for i in range(n):

    current_sum += nums[i]

    if current_sum == 0:
        print('xyz')
        max_len = max(max_len,i + 1)

    pre = - (current_sum)
    print(pre) 
    if pre in prefix:
        max_len= max(max_len,i - prefix[pre])

    prefix[current_sum] = i

print(max_len)

