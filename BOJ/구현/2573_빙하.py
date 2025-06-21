import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

ices = []

dy = [1,0,-1,0]
dx = [0,1,0,-1]

year = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            ices.append((i, j))

def BFS(ice):
    visited = [[False] * M for _ in range(N)]
    count = 1
    q = deque()
    q.append(ice)
    visited[ice[0]][ice[1]] = True
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if graph[ny][nx] != 0 and visited[ny][nx] == False:
                q.append((ny,nx))
                count += 1
                visited[ny][nx] = True
        
        
    
    return count

while ices:
    # 1년 경과
    year += 1
    for idx, a in enumerate(ices):
        y, x = a
        temp_v = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if graph[ny][nx] == 0:
                temp_v += 1
        
        graph[y][x] -= temp_v
        if graph[y][x] <= 0:
            # 빙산 제거
            graph[y][x] = 0
            del ices[idx]
        
    # 빙산 카운트
    if len(ices) > 0:
        if BFS(ices[0]) == len(ices):
            # 빙산 1개
            pass
        else:
            break
    else:
        # 다 녹은 것이므로 0
        year = 0
        break
    # 2이상이면 break
    
print(year)