import sys
from collections import deque
input = sys.stdin.readline
# 그래프를 완성
N = int(input().strip())
graph = [list(input().strip()) for _ in range(N)]
dy = [1,0,-1,0]
dx = [0,1,0,-1]
chk = [[False] * N for _ in range(N)]
chk_ab = [[False] * N for _ in range(N)]
count_normal = 0
count_abnormal = 0
def BFS(j, i, value):
    q = deque()
    q.append((j, i))
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if chk[ny][nx] == False and value == graph[ny][nx]:
                    chk[ny][nx] = True
                    q.append((ny, nx))

def BFS_ab(j, i, value):
    q = deque()
    q.append((j, i))
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if value == 'R' or value == 'G':
                    if chk_ab[ny][nx] == False and (graph[ny][nx] == 'R' or graph[ny][nx] == 'G'):
                        chk_ab[ny][nx] = True
                        q.append((ny, nx))
                else:
                    if chk_ab[ny][nx] == False and value == graph[ny][nx]:
                        chk_ab[ny][nx] = True
                        q.append((ny, nx))

for j in range(N):
    for i in range(N):
        if chk[j][i] == False:
            BFS(j, i, graph[j][i])
            count_normal += 1
        if chk_ab[j][i] == False:
            BFS_ab(j, i, graph[j][i])
            count_abnormal += 1

print(count_normal)
print(count_abnormal)
'''
시간 제한 1초면 몇개까지 가능이지?
100개니까 10,000 
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

정상인용, 적록색약용 2개를 만듬
chk와 chk_ab를 헷갈려서 실수함
'''
