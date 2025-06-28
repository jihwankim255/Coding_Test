import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

# 국가들
arr = [list(map(int, input().split())) for _ in range(N)]
days = 0

# 인구 격차가 범위 이내인지 체크
def isInRange(num1, num2):
    if L <= abs(num1-num2) <= R:
        return True
    else:
        return False

# 전체 국가를 탐색하면서 연합을 구성
def BFS(j, i):
    if chk[j][i] == True: return 
    q = deque()
    temp_union = []
    union_sum = arr[j][i]
    # 연합 길이, 전체 인구 합
    chk[j][i] = True
    q.append((j,i))
    temp_union.append((j,i))
    while q:
        ey, ex = q.popleft()
        for ky, kx in ((-1,0),(1,0),(0,-1),(0,1)):
            ny = ey + ky
            nx = ex + kx
            if 0<=ny<N and 0<=nx<N and chk[ny][nx] == False and isInRange(arr[ey][ex], arr[ny][nx]):
                chk[ny][nx] = True
                q.append((ny, nx))
                union_sum += arr[ny][nx]
                temp_union.append((ny, nx))
    if len(temp_union) > 1:
        unions.append(temp_union)
        unions_meta.append((len(temp_union), union_sum))
    else:
        chk[j][i] = False

while True:
    # 연합들
    unions = []
    unions_meta = []
    
    chk = [[False] * N for _ in range(N)]
    
    # 연합군 생성
    for j in range(N):
        for i in range(N):
            BFS(j, i)
    # 연합 없을 경우 끝
    if len(unions) == 0:
        break
    
    # 연합 있을 경우 인구 평탄화 시행
    for idx, union in enumerate(unions):
        for uy, ux in union:
            arr[uy][ux] = unions_meta[idx][1] // unions_meta[idx][0]
        
    days += 1
    

        

print(days)
        
'''
실수
첫 국가의 인구를 추가하지 않음
unions_sum = 0  =>  unions_sum = arr[j][i]

sum 계산을 연합이 만들어지기 전에 하면 안된다고 생각해서 연합을 다 만든 후에 unions_meta를 만들어서 했는데
어차피 chk로 연합이 없는 경우만 계산하기 때문에 바로바로 sum 계산을 해줘도 상관 없다.

'''