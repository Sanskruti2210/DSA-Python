'''
Given two sorted arrays a and b of size m and n respectively. 
Find the kth element of the final sorted array.
'''

def kthElement(a,b,k):
    
    if len(a) > len(b):
        a,b = b,a
        
    n1 = len(a)
    n2 = len(b)
    
    low = 0
    high = n1
    
    while low <= high:
        
        mid = (low + high)//2
        
        partition2 = k - mid
        
        if mid == 0:
            left1 = float('-inf')
        else:
            left1 = a[mid - 1]
        
        if mid == len(a):
            right1 = float('inf')
        else:
            right1 = a[mid]
                    
        if partition2 == 0:
            left2 = float('-inf')
        else:
            left2 = b[partition2 - 1]
                    
        if partition2 == len(b):
            right2 = float('inf')
        else:
            right2 = b[partition2]
        
        if left1 <= right2 and left2 <= right1 :
            return max(left1,left2)
        elif left1 > right2 :
            high = mid - 1
        elif left2 > right1 :
            low = mid + 1
    
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

res = kthElement(a,b,k)
print(res)
