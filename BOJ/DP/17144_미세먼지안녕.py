'''
직접 큐에 원소를 이동시키는 거보다
index에 대해 for문을 돌고 arr[index_R][index_C]의 값을 변경하는 방식으로 생각해야함

끝에서부터 이전 값을 덮어 씌우는 방식으로 하면 깔끔함
'''
import sys
input = sys.stdin.readline
from collections import deque
R, C, T = map(int, input().split())

arr = deque([])
puri = []
for j in range(R):
    row = deque(list(map(int, input().split())))
    # for i in range(C):
    if row[0] == -1:
        puri.append((j, 0))
    arr.append(row)

        
dy = [1,0,-1,0] 
dx = [0,1,0,-1]

for _ in range(T):
    # 미세먼지 확산
    temp_arr = [[0] * C for _ in range(R)]
    for j in range(R):
        for i in range(C):
            if arr[j][i] > 0:
                v = arr[j][i] // 5
                for k in range(4):
                    ny = j + dy[k]
                    nx = i + dx[k]
                    if 0<=ny<R and 0<=nx<C and arr[ny][nx] != -1:
                        temp_arr[ny][nx] += v
                        arr[j][i] -= v
    
    # 합치기
    for j in range(R):
        for i in range(C):
            arr[j][i] += temp_arr[j][i]
                
    # pprint.pprint(arr)
    # 공기청정기 작동
    # 
    uy, ux = puri[0]
    ly, lx = puri[1]
    for i in range(uy-1, 0, -1): # 왼쪽
        arr[i][0] = arr[i-1][0]
    # 0~ C-1
    for i in range(C-1): # 위쪽
        arr[0][i] = arr[0][i+1]
    # 0~ uy-1
    for i in range(uy): # 오른쪽
        arr[i][-1] = arr[i+1][-1]
    # C~ 1
    for i in range(C-1, 1, -1): # 아래쪽
        arr[uy][i] = arr[uy][i-1]
    
    for i in range(C-1, 1, -1):
        arr[uy][i] = arr[uy][i-1]
    arr[uy][1] = 0

    # # 아래쪽 시계
    for i in range(ly+1, R-1):
        arr[i][0] = arr[i+1][0]
    for i in range(C-1):
        arr[R-1][i] = arr[R-1][i+1]
    for i in range(R-1, ly, -1):
        arr[i][C-1] = arr[i-1][C-1]
    for i in range(C-1, 1, -1):
        arr[ly][i] = arr[ly][i-1]
    arr[ly][1] = 0
        
    
ans = 0

for i in range(R):
    ans += sum(arr[i])
    
print(ans+2)