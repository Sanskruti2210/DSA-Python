'''Print the following pattern for a given N.'''
n = 5

for i in range(1,n + 1):
    
    for j in range(n - i):
        print(" ",end="")
        
    for k in range(i):
        print("*",end="")
        
    for s in range(1,i):
        print("*",end="")
        
    print()
    
for i in range(n,0,-1):
    
    for j in range(n - i):
        print(" ",end="")
        
    for k in range(i):
        print("*",end="")
        
    for s in range(1,i):
        print("*",end="")
        
    print()
    