'''
Given two strings s and goal, return true if and only if s can become goal 
after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
'''

s = "abcde" 
goal = "cdeab"

def rotateString(s,goal):
    
    if s == goal :
        return True
    
    if len(s) != len(goal):
        return False
    
    return goal in (s + s)

result = rotateString(s,goal)
print(result)
    
    
