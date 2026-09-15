"""
You are given two integers n1 and n2.
You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.
"""

n1 = int(input("Enter a num : "))
n2 = int(input("Enter a num : "))

while n1 > 0 and n2 > 0:

    # The Optimal sol to find GCD of two num is using Euclidean Algorithm
    # It stats that :
    # 1. Start with two integers a and b(where a>=b)
    # 2. Divide a by b and find reminder r
    # 3. Replace a with b and b with r : a <- b  b <- r
    # 4. Do this process untill any of a or b becomes zero. If any becomes zero then other is the GCD
    # The importanat part is find which num is greater between a and b and then do process accordingly.
    # For Example :
    # GCD(13,11)
    # 13>11 => 13%11 = 2
    # 11>2 => 11%2=1
    # 2>1 => 2%1==0
    # So GCD = 1
    if n1 > n2:
        n1 = n1 % n2
    else:
        n2 = n2 % n1

if n1 == 0:
    print("GCD : ", n2)
else:
    print("GCD : ", n1)
