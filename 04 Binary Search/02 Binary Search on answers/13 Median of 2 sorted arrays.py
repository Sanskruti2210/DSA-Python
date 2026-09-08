'''
Given two sorted arrays arr1 and arr2 of size m and n respectively,
return the median of the two sorted arrays.
The median is defined as the middle value of a sorted list of numbers. 
In case the length of the list is even, the median is the average of the two middle elements.
'''

def median(arr1,arr2):
    
    n1 = len(arr1)
    n2 = len(arr2)
    
    if n1 > n2:
        arr1,arr2 = arr2,arr1
        n1,n2 = n2,n1
        
    low = 0
    high = len(arr1)
    ans = 0
    
    while low <= high:
        
        mid = (low + high)//2
        
        partition2 = (n1 + n2 + 1)//2 - mid
        
        if mid == 0:
            left1 = float('-inf')
        else:
            left1 = arr1[mid - 1]

        if mid == len(arr1):
            right1 = float('inf')
        else:
            right1 = arr1[mid]
            
        if partition2 == 0:
            left2 = float('-inf')
        else:
            left2 = arr2[partition2 - 1]
            
        if partition2 == len(arr2):
            right2 = float('inf')
        else:
            right2 = arr2[partition2]
                
        if left1 <= right2 and left2 <= right1 :
            if ( n1 + n2 ) % 2 != 0:
                ans = max(left1,left2)
            else :
                ans = (max(left1,left2) + min(right1,right2))/2
            break
        elif left1 > right2 :
            high = mid - 1
        elif left2 > right1 :
            low = mid + 1
            
    return ans

arr1 = [1,2]
arr2 = [3,4]

res = median(arr1,arr2)
print(res)