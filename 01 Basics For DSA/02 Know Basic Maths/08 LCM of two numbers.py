'''
You are given two integers n1 and n2. You need find the Lowest Common Multiple (LCM) 
of the two given numbers. Return the LCM of the two numbers.
The Lowest Common Multiple (LCM) of two integers is the lowest positive integer that is 
divisible by both the integers.
'''

def LCM(n1,n2):
    
    lcm = 0
    
    for i in range(min(n1,n2),(n1*n2) + 1):
        
        # If i is divisible by both n1 and n2
        if i % n1 == 0 and i % n2 == 0:
            lcm = i
            break
        
        
    return lcm

n1 = 4
n2 = 6
ans = LCM(n1,n2)
print(ans)


