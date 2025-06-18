import sys
input = sys.stdin.readline

N, M = map(int, input().split())
 
graph = [list(map(int,input().split())) for _ in range(N)]


answer = 0

def solution(i, j):
    temp = []
    # 1-1
    if j+3 < M:
        v = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i][j+3]
        temp.append(v)
    # 1-2
    if i+3 < N:
        v = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j]
        temp.append(v)
    # 2-1
    if j+1 < M and i+1 < N:
        v = graph[i][j] + graph[i+1][j] + graph[i][j+1] + graph[i+1][j+1]
        temp.append(v)
    # 3-1
    if i+2 < N and j+1 < M:
        v = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j+1]
        temp.append(v)
    # 3-2
    if i+2 < N and j-1 >= 0:
        v = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j-1]
        temp.append(v)
    # 3-3
    if i+2 < N and j+1 < M:
        v = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i][j+1]
        temp.append(v)
    # 3-4
    if i+2 < N and j+1 < M:
        v = graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j+1]
        temp.append(v)
    # 3-5
    if i+1 < N and j+2 < M:
        v = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j+2]
        temp.append(v)
    # 3-6
    if i+1 < N and j+2 < M:
        v = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j]
        temp.append(v)
    # 3-7
    if i+1 < N and j-2 >= 0:
        v = graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+1][j-2]
        temp.append(v)
    # 3-8
    if i+1 < N and j+2 < M:
        v = graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2]
        temp.append(v)
    # 4-1
    if i+2 < N and j+1 < M:
        v = graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1]
        temp.append(v)
    # 4-2
    if i+2 < N and j-1 >= 0:
        v = graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+2][j-1]
        temp.append(v)
    # 4-3
    if i+1 < N and j-1 >= 0 and j+1 < M:
        v = graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i][j+1]
        temp.append(v)
    # 4-4
    if i+1 < N and j+2 < M:
        v = graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j+2]
        temp.append(v)
    # 5-1
    if i+1 < N and j+2 < M:
        v = graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i][j+2]
        temp.append(v)
    # 5-2
    if i+1 < N and j-1 >= 0 and j+1 < M:
        v = graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+1][j+1]
        temp.append(v)
    # 5-3
    if i+2 < N and j-1 >= 0:
        v = graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+2][j]
        temp.append(v)
    # 5-4
    if i+2 < N and j+1 < M:
        v = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+1][j+1]
        temp.append(v)
    if temp:
        return max(temp)
    else:
        return 0


for i in range(N):
    for j in range(M):
        v = solution(i, j)
        answer = max(answer, v)
        
print(answer)

'''
다른 풀이 DFS

'''

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]

v= [[0] * M for _ in range (N)] # dfs 방문 표시 배열

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(n, temp, lst) :
    global ans

    # 종료 조건
    if n == 4 :
        ans = max(temp, ans)
        return
    
    # 재귀 함수 호출 (자기 위치에서 뻣어나가기, 백트래킹)
    for cx, cy in lst :
        for i in range (4) :
            nx, ny = cx + dx[i], cy + dy[i]
            # 범위, 방문 검사
            if 0 <= nx < N and 0<= ny < M and v[nx][ny] == 0 :
                v[nx][ny] = 1
                dfs(n+1, temp + arr[nx][ny], lst + [(nx, ny)])
                v[nx][ny] = 0 # 방문표시 해제로 백트래킹


ans = 0

for i in range (N) :
    for j in range (M) :
        v[i][j] = 1
        dfs(1, arr[i][j], [(i,j)])

print(ans)
