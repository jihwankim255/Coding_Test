'''
https://www.youtube.com/watch?v=ansd5B27uJM&list=PLi-xJrVzQaxXC2Aausv_6mlOZZ2g2J6YB&index=3
https://www.acmicpc.net/problem/1926
개발자장고 BFS 기본 문제
# 아이디어

# 시간 복잡도
O(V+E)
V: m * n
E: V * 4 (V하나에 4개라 넉넉잡아)
= 5V = 5 * m * n = 100만 < 2억 가능

# 자료구조
- 그래프 전체 지도: int[][]
- 방문: bool[][]
- Queue(BFS)

'''
import sys  # 입출력 빠르게 하는 코드 습관화
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs


cnt = 0
maxv = 0

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j, i))
            
print(cnt)
print(maxv)





# import sys
# from collections import deque
# input = sys.stdin.readline
# n, m = map(int, input().split())
# map = [list(map(int, input().split())) for _ in range(n)]
# chk = [[False] * m for _ in range(n)]

# cnt = 0
# maxv = 0

# dy = [-1,0,1,0]
# dx = [0,1,0,-1]

# def bfs(j, i):
#     rs = 1
#     q = deque()
#     q.append((j, i))
#     while q:
#         ey, ex = deque.popleft(q)
#         for i in range(4):
#             ny = ey + dy[i]
#             nx = ex + dx[i]
#             if 0 <= ny < n and 0 <= nx < m:
#                 if map[ny][nx] == 1 and chk[ny][nx] == False:
#                     chk[ny][nx] = True
#                     rs += 1
#                     q.append((ny, nx))
#     return rs


# for j in range(n):
#     for i in range(m):
#         if map[j][i] == 1 and chk[j][i] == False:
#             chk[j][i] = True
#             cnt += 1
#             maxv = max(maxv, bfs(j, i))
# print(cnt) 
# print(maxv)