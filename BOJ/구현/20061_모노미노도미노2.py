'''
pop, del과 같이 요소를 제거하는 메서드를 사용할때
index가 하나씩 밀리는 부분 생각해야함. 역순으로 지우거나, 나중에 한번에 지우기

블루보드를 90도 회전시켜서 하는 방식도 가능

블루보드에 1x2를 이동하는 경우, 그린보드에 2x1을 이동하는 경우
'''


import sys
input = sys.stdin.readline
from collections import deque
N = int(input())

commands = [tuple(map(int,input().split())) for _ in range(N)]

score = 0

blocks = [[()],[(0,0)], [(0,0),(0,1)], [(0,0),(1,0)]]

blue_board = deque([deque([0,0,0,0,0,0]) for _ in range(4)])
green_board = deque([deque([0,0,0,0]) for _ in range(6)])

for (t,x,y) in commands: # 10,000
    # 파랑 이동
    ny = 0
    while True:
        flag = True
        for block in blocks[t]:
            nx = x + block[0]
            ty = ny + block[1]  # ny에도 block[1]을 더해주어야함!
            if ty > 5 or blue_board[nx][ty] != 0:
                flag = False
                break
        if flag:
            ny += 1
        else:
            # 놓기
            ny -= 1
            for block in blocks[t]:
                nx = x + block[0]
                ty = ny + block[1]
                blue_board[nx][ty] = 1
            break   
        
    # 초록 이동
    nx = 0
    while True:
        flag = True
        for block in blocks[t]:
            tx = nx + block[0]  # 행 위치
            ty = y + block[1]   # 열 위치
            if tx > 5 or green_board[tx][ty] != 0:
                flag = False
                break
        if flag:
            nx += 1
        else:
            nx -= 1  # 직전 위치가 최종 위치
            for block in blocks[t]:
                tx = nx + block[0]
                ty = y + block[1]
                green_board[tx][ty] = 1
            break

    
    
    # 초록,파랑에서 사라지는 부분을 지우고 스코어 1 증가
    # 파랑색에서 사라지는 부분 체크
    b_lines = 0
    remove_cols = []
    for i in range(2,6):
        if sum(blue_board[j][i] for j in range(4)) == 4:
            remove_cols.append(i)

    for col in sorted(remove_cols, reverse=True):
        for row in range(4):
            del blue_board[row][col]
        b_lines += 1

    for row in range(4):
        for _ in range(b_lines):
            blue_board[row].appendleft(0)

    score += len(remove_cols)
    
    # 초록 색 사라지는 부분
    g_lines = 0
    for i in reversed(range(2,6)):
        total = sum(green_board[i])
        if total == 4:
            score += 1
            del green_board[i]
            g_lines += 1
    for _ in range(g_lines):
        green_board.appendleft(deque([0,0,0,0]))
    
            
    light_line = 0
    if sum(blue_board[i][0] for i in range(4)) > 0:
        light_line += 1
    if sum(blue_board[i][1] for i in range(4)) > 0:
        light_line += 1
    for _ in range(light_line):
        for i in range(4):
            blue_board[i].pop()
            blue_board[i].appendleft(0)

    light_line = 0
    if sum(green_board[0]) > 0:
        light_line += 1
    if sum(green_board[1]) > 0:
        light_line += 1
    for _ in range(light_line):
        green_board.pop()
        green_board.appendleft(deque([0,0,0,0]))


blue_sum = 0
green_sum = 0
for i in range(4):
    blue_sum += sum(blue_board[i])

for j in range(2,6):
    green_sum += sum(green_board[j])

print(score)
print(blue_sum+green_sum)