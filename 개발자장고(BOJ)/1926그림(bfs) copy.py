'''
https://www.youtube.com/watch?v=ansd5B27uJM&list=PLi-xJrVzQaxXC2Aausv_6mlOZZ2g2J6YB&index=3
https://www.acmicpc.net/problem/1926
개발자장고 BFS 기본 문제
# 아이디어

# 시간 복잡도
O(V+E)
V: m * n
E: V * 4 (V하나에 4개라 넉넉잡아)
= 5V = 5 * m * n = 100만 < 2억 가능!

# 자료구조
- 그래프 전체 지도: int[][]
- 방문: bool[][]
- 뼈뎓(BFS)

'''
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]

chk = [[False] * M for _ in range(N)] 


cnt = 0
maxv = 0
# 상 하 좌 우
dy = [1,0,-1,0]
dx = [0,1,0,-1]

def bfs(y, x):
    rs = 1
    queue = [(y, x)]
    
    while queue:
        ey, ex = queue.pop(0)
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            i
    
    return


for j in range(N):
    for i in range(M):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j, i))
             
            
print(cnt)
print(maxv)