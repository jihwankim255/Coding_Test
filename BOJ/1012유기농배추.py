'''
https://www.acmicpc.net/problem/1012
dfs
테스트케이스가 머임?


'''

# n, m = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(m)]


T = int(input())

dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs( i,j, visited):
    visited[j][i] = True
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0<=nx<M and 0<=ny<N:
            if not visited[ny][nx] and graph[j][i]==1:
                dfs(nx, ny, visited)
    
    
# 가로: M x i
# 세로: N y j
for i in range(T):
    M, N, K = map(int, input().split())
    graph = [ [0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    
    for i in range(M):
        for j in range(N):
            if not visited[j][i] and graph[j][i]==1:
                dfs(i,j, visited)
                count += 1
                
    print(count)