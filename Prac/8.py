'''Given an integer N, return its reverse.'''

n = 12345
temp = n
digits = 0
rev = 0

while n > 0 :
    
    digits += 1
    n = n // 10
    
print(digits)
while  temp > 0 :
    
    rev += (temp % 10)*(10**digits)
    digits -= 1
    temp = temp // 10
    
print(rev // 10)