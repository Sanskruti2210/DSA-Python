'''Given two integers N1 and N2, find their Greatest Common Divisor (GCD).'''

n1 = 20
n2 = 28

while n1 > 0 and n2 > 0:
    
    if n1 > n2:
        n1 = n1%n2
    else:
        n2 = n2%n1
        
if n1 == 0:
    print(n2)
else:
    print(n1)