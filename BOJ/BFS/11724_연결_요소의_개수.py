import sys
from collections import deque
input = sys.stdin.readline
# 정점, 간선
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