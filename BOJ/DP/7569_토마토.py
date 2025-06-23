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
# graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
graph = []
days = 0

total_tomatos = 0
m_tomatos = []

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
dz = [-1, 1]

# 언제 끝나는지? 전체 토마토 수 = 익은 토마토 수 일 때 종료  5 3 2 M, N, H
for h in range(H):
    col = []
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(M):
            if row[m] == 0:
                total_tomatos += 1
            elif row[m] == 1:
                total_tomatos += 1
                m_tomatos.append((h, n, m))
        col.append(row)
    graph.append(col)

q = deque()
if total_tomatos == len(m_tomatos):
    print(0)
else:
    for i in m_tomatos:
        q.append(i)

while q:
    days += 1
    # 익은 토마토 주변을 익은 토마토로 바꿈
    for _ in range(len(q)):
        ez, ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < N and 0 <= nx < M and graph[ez][ny][nx] == 0:
                graph[ez][ny][nx] = 1
                m_tomatos.append((ez, ny, nx))
                q.append((ez, ny, nx))
        # z축에 대해 진행
        for i in range(2):
            nz = ez + dz[i]
            if 0 <= nz < H and graph[nz][ey][ex] == 0:
                graph[nz][ey][ex] = 1
                m_tomatos.append((nz, ey, ex))
                q.append((nz, ey, ex))
    # 전체가 다 익었는지 체크
    if total_tomatos == len(m_tomatos):
        print(days)
        break
    # 1. 전체 다 익었을 경우 종료
    # 2. 덜익었을 경우 계속.
if total_tomatos != len(m_tomatos):
    print(-1)
    
    
'''
day를 토마토와 같이 넣으면 따로 for문을 쓸 필요 없음
for문을 쓰는 이유가 day가 바뀔 때마다 모두 비워내서 날짜를 구분하기 위해선데
day를 같이 인자로 전달하면 그럴 필요 없음. 대신 max 써야함


'''