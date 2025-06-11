import sys
input = sys.stdin.readline

# n = int(input()) # 사람 수
# a, b = map(int, input().split())

# graph = [[] for _ in range(n+1)]
# chk = [False] * (n+1)

# m = int(input())
# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)
    
# each = 0
# print(graph)


# def dfs(a, b):
#     if b in graph[a]:
#         return
#     for i in graph[a]:
#         if chk == False:
#             each += 1
#             chk[i] = True
#             dfs(i, b)
    

# print(dfs(a, b))
#=======================================================================
''' result를 쓰는거만 다름 '''
# N = int(input())
# A, B = map(int, input().split())
# M = int(input())
# graph = [[] for _ in range(N+1)]
# visited = [False] * (N+1)
# result = []

# for _ in range(M):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# def dfs(v, num):
#     num += 1
#     visited[v] = True
    
#     if v == B:
#         result.append(num)
    
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i, num)



# dfs(A, 0)

# if len(result) == 0:
#     print(-1)
# else:
#     print(result[0]-1)

import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []
flag = False
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(v, num):
    num += 1
    visited[v] = True
    if v == B:
        global flag
        flag = True
        print(num-1)
        return
    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

dfs(A, 0)
if flag == False:
    print(-1)



