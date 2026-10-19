'''Given an integer N, determine whether it is a palindrome.'''

num = 121
temp = num
rev = 0

while num > 0:
    
    rmd = num % 10
    rev = rev*10 + rmd
    num = num // 10
    
if rev == temp:
    print(True)
else:
    print(False)