from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# print(graph)

dy = [1,0,-1,0]
dx = [0,1,0,-1]

time = 0

cheeses = []
# 치즈 추가
for j in range(N):
    for i in range(M):
        if graph[j][i] != 0:
            cheeses.append((j, i))
cheeses_count = 0

def BFS(j, i):
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((j, i))
    visited[j][i] = True
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0<=ny<N and 0<=nx<M and visited[ny][nx] == False:
                visited[ny][nx] = True
                if graph[ny][nx] == 0:
                    q.append((ny, nx))
                elif graph[ny][nx] == 1:
                    # 치즈 녹이기
                    graph[ny][nx] = 0
                    cheeses.remove((ny, nx))

while True:
    # 치즈 개수 저장해두기
    cheeses_count = len(cheeses)
    # 1초 경과
    time += 1
    # 치즈 녹이기
    BFS(0, 0)
    # 치즈가 모두 녹았는가?
    if len(cheeses) == 0:
        break

print(time)
print(cheeses_count)
    

'''
겉부분을 어떻게 알지?
0,0 에서 BFS로 탐색해서 만나는 부분을 지움

remove로 요소 제거

'''