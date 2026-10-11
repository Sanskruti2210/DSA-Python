'''
Given an integer M and an undirected graph with N vertices (zero indexed) and E edges. 
The goal is to determine whether the graph can be coloured with a maximum of M colors so 
that no two of its adjacent vertices have the same colour applied to them.
In this context, colouring a graph refers to giving each vertex a different colour. 
If the colouring of vertices is possible then return true, otherwise return false.
'''

N = 5 
M = 3 
E = 6 
Edges = [ (0, 1) , (1, 2) , (0, 2) , (2,3) , (2,4) , (3,4) ]

# Create adjacency list
graph = [[] for _ in range(N)]

for u, v in Edges:
    graph[u].append(v)
    graph[v].append(u)

# 0 means uncolored
color = [0] * N

def is_safe(node, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False

    return True

def solve(node):
    # All vertices are colored
    if node == N:
        return True

    # Try every color from 1 to M
    for c in range(1, M + 1):

        if is_safe(node, c):

            # Assign color
            color[node] = c

            # Try coloring the next vertex
            if solve(node + 1):
                return True

            # Backtrack
            color[node] = 0

    return False


print(solve(0))
print(color)