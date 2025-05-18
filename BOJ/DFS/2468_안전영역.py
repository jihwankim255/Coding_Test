import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
maxv = 0


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def BFS(y, x):
    Q = deque()
    Q.append((y, x))
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx] > height and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    Q.append((ny, nx))
    
rs = []
for k in range(100):    
    height = k + 1
    chk = [[False] * N for _ in range(N)]
    # 안 잠긴 지점
    count = 0
    for j in range(N):
        for i in range(N):
            if graph[j][i] > height and chk[j][i] == False:
                chk[j][i] = True
                BFS(j, i)
                count += 1
    rs.append(count)

print(max(rs))
'''
[]
N  2  ~ 100
1   ~   100

다 잠기기 직전? N^2이면 닫잠긴거고 
다잠기기 직전이 답일수도?
100 100인데
높이 99가 답일수도?

5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
'''