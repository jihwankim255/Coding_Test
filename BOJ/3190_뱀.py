import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
K = int(input())

apples = [tuple(map(int,input().split())) for _ in range(K)]

L = int(input())
directions = {}
dir_key = []
for i in range(L):
    x, y = input().split()
    dir_key.append((int(x)))
    
    directions[int(x)] = y

# print(apples)
# print(directions)
# print(dir_key)

dy = [0,1,0,-1]
dx = [1,0,-1,0]
a = 0
q = deque()
q.append((1,1))

time = 0

def check(next_v):
    if 0 < next_v[0] <= N and 0 < next_v[1] <= N and (next_v not in q):
        return False
    else:
        return True

def isApple(next_v):
    flag = False
    for idx, a in enumerate(apples):
        if a == next_v:
            # print('apple', a, next_v)
            flag = True
            del apples[idx]
            
    
    if flag:
        return True
    else:
        return False
    
while True:
    time += 1
    # 다음칸 이동
    # 현재 위치에서
    cur = q[-1]
    next_v = (cur[0]+dy[a], cur[1]+dx[a])
    # 끝났는지 체크
    if check(next_v):
        break
    q.append(next_v)
    if isApple(next_v):
        # 사과가 있으면?
        pass
    else:
        # 사과가 없으면?
        # 꼬랑지 자르기
        q.popleft()
        pass
    # 방향 전환
    if time in dir_key:
        if directions[time] == 'D':
            a = (a + 1) % 4
        elif directions[time] == 'L':
            a = (a + 4 - 1) % 4
        
        
print(time)

'''

딕셔너리에 저장하는 법

'''