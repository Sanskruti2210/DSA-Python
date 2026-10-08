'''
Given an integer M and an undirected graph with N vertices (zero indexed) and E edges. 
The goal is to determine whether the graph can be coloured with a maximum of M colors so 
that no two of its adjacent vertices have the same colour applied to them.
In this context, colouring a graph refers to giving each vertex a different colour. 
If the colouring of vertices is possible then return true, otherwise return false.
'''

def compress(index, s, count, res):
    
    if index == len(s):
        res.append(s[index - 1] + str(count))
        return

    if s[index] == s[index - 1]:
        compress(index + 1, s, count + 1, res)
    else:
        res.append(s[index - 1] + str(count))
        compress(index + 1, s, 1, res)


s = 'aaabbcde'
res = []

compress(1, s, 1, res)

print("".join(res))