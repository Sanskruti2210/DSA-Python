'''
Given an integer N, determine whether it is an Armstrong number.
An Armstrong number is a number where the sum of each digit raised to the power 
of the number of digits equals the original number.
'''

def armStrong(num):
    
    digit = len(str(num))
    sum = 0
    temp = num
    
    while num > 0:

        sum += (num%10)**digit
        num = num // 10
        
    if temp == sum:
        return True
    else:
        return False

num = 153
print(armStrong(num))