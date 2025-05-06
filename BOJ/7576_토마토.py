import sys
from  collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

tmap = [ list(map(int, input().split())) for _ in range(N) ]


dy = [1,0,-1,0]
dx = [0,1,0,-1]

def BFS(tmap):
    day = 0
    total_0 = 0
    total_1 = 0
    queue = deque()  # [(0,0), (3, 5)]
    for r, row in enumerate(tmap):
        for c, col in enumerate(row):
            if col == 0:
                total_0 += 1
            elif col == 1:
                queue.append((r, c))
    
    while queue:
        queue_len = len(queue)
        for _ in range(queue_len):
            v = queue.popleft()
            for i in range(4):
                ny = v[0] + dy[i]
                nx = v[1] + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if tmap[ny][nx] == 0:
                        tmap[ny][nx] = 1
                        queue.append((ny, nx))
                        total_1 += 1
        day += 1
            
        
    if total_0 == total_1:
        return day -1
    else:
        return -1

print(BFS(tmap))