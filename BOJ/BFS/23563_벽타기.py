'''
아이디어
움직일수 없거나 E에 도착하면 중단
최소값과 비교

시간복잡도
H W
#####
#..E#
#.S.#
#...#
#####
자료구조
큐

0 0 0 0 0
0 0 1 E 0
0 1 S 1 0
0 0 1 0 0
0 0 0 0 0

''' 


import sys
from math import inf
from collections import deque
input = sys.stdin.readline


dir = [(-1,0), (1,0), (0,-1),(0,1)]

H, W = map(int, input().split())
# 전체 주어진 맵
matrix = [input().strip() for _ in range(H)]

# 각 위치별 가중치 (chk와 비슷) 0: 벽과인접, 1: 인접x, 2: 벽
w = [[1] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if matrix[i][j] == '#':
            w[i][j] = 2
            continue
        if matrix[i][j] == 'S':
            si = i
            sj = j
        elif matrix[i][j] == 'E':
            ei = i
            ej = j
        for di, dj in dir:
            if 0<= i + di < H and 0 <= j + dj < W and matrix[i + di][j + dj] == '#':
                w[i][j] = 0
                break

dq = deque([(0, si, sj)])
distance = [[inf] * W for _ in range(H)]
distance[si][sj] = 0

while dq:
    d, i, j = dq.popleft()
    if distance[i][j] < d:
        continue
    for di, dj in dir:
        if 0<= i + di < H and 0 <= j + dj < W:
            if not w[i][j] and not w[i + di][j + dj]:
                if distance[i + di][j + dj] > d:
                    distance[i + di][j + dj] = d
                    dq. appendleft((d, i + di, j + dj))
            elif w[i + di][j + dj] != 2:
                if distance[i + di][j + dj] > d + 1:
                    distance[i + di][j + dj] = d + 1
                    dq.append((d + 1, i + di, j + dj))
                    
print(distance[ei][ej])