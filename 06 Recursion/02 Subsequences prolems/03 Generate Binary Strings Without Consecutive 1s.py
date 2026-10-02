'''
Given an integer n, return all binary strings of length n that do not contain consecutive 1s. 
Return the result in lexicographically increasing order.
A binary string is a string consisting only of characters '0' and '1'.
'''

def binaryString(i,n,string,ans):
    
    # Base Case
    if i == n:
        ans.append(string)
        return 
        
    # Pick 0     
    binaryString(i + 1,n,string + '0',ans)
        
    # Pick 1
    if string == '' or string[-1] == '0':

        binaryString(i + 1,n,string + '1',ans)
    
        
n = 4
ans = []
string = ''
binaryString(0,n,string,ans)
print(ans)