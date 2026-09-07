'''
Given a sorted array arr of size n, containing integer positions of n gas stations on the X-axis, 
and an integer k, place k new gas stations on the X-axis.
The new gas stations can be placed anywhere on the non-negative side of the X-axis, including non-integer positions.
Let dist be the maximum distance between adjacent gas stations after adding the k new gas stations.
Find the minimum value of dist.
Your answer will be accepted if it is within 1e-6 of the true value.
'''

import math

def countStation(arr,mid):
    
    # Init totalStation
    totalStation = 0
    
    for i in range(1,len(arr)):
        
        # Find gap between two adjencent
        gap = arr[i] - arr[i - 1]
        
        # Station will be gap/mid - 1 
        # For example gap = 6 mid = 2 so the station inside that gap will be 
        # 2 by formula it will be like stations = ceil(6/2) - 1 = 3 - 1 = 2
        # Here we do -1 as the one station will be always be from the first one 
        stations = math.ceil(gap / mid) - 1
        
        # Add it into totalStation
        totalStation += stations
       
    return totalStation

def minDistance(arr,k,n):
    
    low = 0
    high = 0

    # The max possible distance would be max dis between any two adjencent
    for i in range(1,len(arr)):
        high = max( high , arr[i] - arr[i - 1] )
    
    # Here we write high - low >= 1e-6 bcz we need the closet possible ans it can be anything
    while high - low >= 1e-6 :
        
        # Compute mid
        mid = ( low + high ) / 2
        
        # Count total station for given mid
        totalStation = countStation(arr,mid)
        
        # Search on left half for more smalller value
        if totalStation <= k :
            high = mid
            
        # Else search on right half
        else :
            low = mid
            
    return float(high)
    
n = 10
arr = [0,13,27,40,58,75]
k = 9

res = minDistance(arr,k,n)
print(f'{res:0.2f}')
