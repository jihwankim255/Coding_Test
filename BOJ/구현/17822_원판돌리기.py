'''
# 이문제의 핵심
nx = (cx + dx) % M 
원판에서 첫번째와 마지막 수는 이어져 있으므로
-1 % 4 = 1

'''


import sys
input = sys.stdin.readline
from collections import deque

N, M, T = map(int, input().split())

arr = [deque(map(int, input().split())) for _ in range(N)]

# x, d, k  (2 0 1)
cmd = [list(map(int, input().split())) for _ in range(T)]

# 시계 방향으로 회전
# 인접하면서 같은 수가 존재하면 제거
# 존재하지 않으면 평균보다 큰수에-1, 작은수에 +1

def rotate(x,d,k):
    # 돌려야 하는 원판
    pan_num = [i for i in range(x-1,N,x)]
    # 돌려야 하는 바퀴
    kan = k % M
    if d == 0:
        # 시계 방향
        # num 번째 판
        for num in pan_num:
            # 이동
            for _ in range(kan):
                v = arr[num].pop()
                arr[num].appendleft(v)
    else:
        # 반시계 방향
        for num in pan_num:
            for _ in range(kan):
                v = arr[num].popleft()
                arr[num].append(v)

def cal(x,d,k):
    rotate(x,d,k)
    flag = False
    chk = [[False] * M for _ in range(N)]
    sum = 0
    count = 0
    for j in range(N):
        for i in range(M):
            if arr[j][i] != 0:
                count += 1
                sum += arr[j][i]
                q = deque()
                q.append((j, i))
                chk[j][i] = True
                should_change = [(j, i)]
                while q:
                    cy, cx = q.popleft()
                    for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
                        ny = cy + dy
                        nx = (cx + dx) % M 
                        if 0<=ny<N and 0<=nx<M and chk[ny][nx]==False:
                            if arr[cy][cx] == arr[ny][nx]:
                                chk[ny][nx] = True
                                flag = True
                                should_change.append((ny,nx))                            
                                q.append((ny, nx))
                if len(should_change) > 1:
                    for y,x in should_change:
                        arr[y][x] = 0
    if sum == 0:
        return
    if not flag:
        avg = sum / count
        for j in range(N):
            for i in range(M):
                if arr[j][i] != 0:
                    if arr[j][i] > avg:
                        arr[j][i] -= 1
                    elif arr[j][i] < avg:
                        arr[j][i] += 1
        
ans = 0

for x, d, k in cmd:
    cal(x,d,k)
    total = 0
    for ar in arr:
        total += sum(ar)
    ans = total
    if total == 0:
        break
    # print('tt: ',total)
print(ans)


# 원판에 적힌 수의 합 계산
# for j in range(N):
#     for i in range(M):
#         sum += arr[j][i]
# print(sum)