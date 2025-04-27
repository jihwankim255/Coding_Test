import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
# graph를 구한다
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
count = 0
visit = [False] * (N+1)
for  i in range(N):
    if visit[i+1] == False:
        queue = deque()
        queue.append(i+1)
        # visit[i+1] = True

        while queue:
            v = queue.popleft()
            if visit[v] == False:
                visit[v] = True
                queue+=graph[v]

        count+=1
print(count)

#& 다른 풀이
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 함수
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0 # 연결 노드의 수
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1 # dfs 한 번 끝날 때마다 count+1

print(count)