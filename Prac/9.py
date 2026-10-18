'''Q10 — Koko Eating Bananas 🍌
Koko has n piles of bananas. piles[i] represents the number of bananas in the i-th pile.
She has h hours to eat all the bananas.
Each hour, she chooses one non-empty pile and eats k bananas from it. If fewer than k bananas remain, 
she eats all the remaining bananas from that pile.
Find the minimum value of k such that she can finish all bananas within h hours.'''

import math

def count(piles,mid,hour):
    
    count = 0
    
    for i in range(len(piles)):
        count += math.ceil(piles[i] / mid)
        
    return count

def kokoBanana(piles,hour):
    
    low = 1
    high = h
    
    while low <= high:
        
        mid = (low + high) // 2
        
        countBanana = count(piles,mid,hour)
        
        if countBanana <= h:
            high = mid - 1
            
        else:
            
            low = mid + 1
            
    return low

piles = [3, 6, 7, 11]
h = 8
print(kokoBanana(piles,h))