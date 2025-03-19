'''
BFS 를 돌면서 탐색

먹을수 없었다가 사이즈가 커져서 먹을수 있어질 수 있음 chk를 나중에?

거리가 가까운 물고기가 많다면? 가장위, 왼쪽 

1 0 0
0 2 1
0 9 0

사이즈가 아니라 거리니까 DFS로 해야됨
'''


import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int,input().split())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

time = 0
shark_size = 2

# 상어 위치 찾기
for j in range(N):
    for i in range(N):
        if map[j][i] == 9:
            shark_position = (j, i)
            chk[j][i] = True

dy = [-1,0,1,0]
dx = [0,1,0,-1]
find = False

# 먹이 탐색 BFS
def DFS(position):
    global find
    if find:
        return
    ey, ex = position
    if shark_size > map[ey][ex] and map[ey][ex] != 0:
        find = True
        print("rs: ", position)
        return position
    
    for i in range(4):
        ny = ey + dy[i]
        nx = ex + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if shark_size >= map[ny][nx]:
                DFS((ny, nx))



print('!!: ',DFS(shark_position))





# print(time)