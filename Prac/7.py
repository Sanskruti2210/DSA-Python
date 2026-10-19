'''Given a positive integer N, count the number of digits in it.'''

n = 58392
digits = 0

while n > 0 :
    
    digits += 1
    n = n // 10
    
print(digits)