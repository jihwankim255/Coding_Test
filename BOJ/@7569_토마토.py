'''
3차원을 어떻게 배열에 담지?

[[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]
],
[[0,0,0,0,0],
[0,0,0,1,0],
[0,0,0,0,0]
]]

몇번째 날인지 튜플에 저장하는 방식 -> 

'''


from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
count = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                queue.append((h, n, m, 0))
            elif graph[h][n][m] == 0:
                count += 1

dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]

max_day = 0
while queue:
    z, y, x, day = queue.popleft()
    max_day = max(max_day, day)
    for d in range(6):
        nz = z + dz[d]
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                count -= 1
                queue.append((nz, ny, nx, day + 1))

print(max_day if count == 0 else -1)

