"""
You are given an integer n. You need to
check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
An armstrong number is a number which is equal to the sum of the digits of the number,
raised to the power of the number of digits.
"""

n = int(input("Enter a num : "))

temp = n
armstrong = 0
digits = len(str(n))
print(digits)

while n > 0:

    # To find armstrong num first found out the num of digits in num and then calculate the sum of digit^numOfDigit
    # For Example :
    # 370 => num of Digits : 3
    # 370%10 => rmd = 0 => armstrong = 0+0^3 = 0 => 370//10 = 37
    # 37%10 => rmd = 7 => armstrong = 0+7^3 = 343 => 37//10 = 3
    # 3%10 => rmd = 3 => armstrong = 343 + 3^3 = 343+27 = 370 => 3//10 = 0
    # Therefore 370 is armstrong num
    rmd = n % 10
    armstrong = armstrong + rmd**digits
    n //= 10

print(armstrong)
if temp == armstrong:
    print("True")
else:
    print("False")
