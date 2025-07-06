'''
주사위값을 어떻게 구하지?
보는 방향에 따라도 다른 값임

# 자료구조
각 면의 숫자
dice: list[int] = []
바닥에 닿는 면
cur_idx 

바닥에 닿는 면을 바꾸는 방식으로 하면, 두번째 이후부터 상대적인 위치가 꼬이게됨
바닥면은 고정한채 숫자를 이동해야함.
인덱스를 하나만 저장하고 나머지를 상대적 위치로 찾으려고 하면 불가능
6면 모두 저장해야 함
'''

import sys
input = sys.stdin.readline

N, M, y, x, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dir = [(0,0),(0, 1),(0, -1),(-1, 0),(1, 0)]

dice: list[int] = [0, 0,0,0,0,0,0]


def get_dice_indx(dir):
    if dir == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif dir == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif dir == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif dir == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

def get_opposite_idx(cur):
    return abs(7-cur)

# 커맨드에 for문을 돌림
for command in commands:
    # 주사위 이동
    ny = y + dir[command][0]
    nx = x + dir[command][1]
    if 0<=ny<N and 0<=nx<M:
        get_dice_indx(command)
        y, x = ny, nx
        if graph[ny][nx] == 0:
            graph[ny][nx] = dice[6]
        else:
            dice[6] = graph[ny][nx]
            graph[ny][nx] = 0
        print(dice[1])

# 지도 칸이 0인 경우 동작

# 지도 칸이 0이 아닌 경우 동작

# 위에 있는 숫자 출력


'''
# 자료구조
n1,n2,n3,n4,n5,n6

자료구조는 나와 거의 비슷함. 주사위 각면을 변수로 함.
1풀이
cur_dix로 현재 바닥에 닿은 부분을 옮겨감

주사위 면을 고정시키고 숫자를 이동하는 방식


'''