'''
https://school.programmers.co.kr/learn/courses/30/lessons/86052
Lv. 2	2,970명	16%
실상 레벨3다
'''

def solution(grid):
    result = []
    n = len(grid) 
    m = len(grid[0]) 
    grid = [[char for char in row] for row in grid]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x, y = 0, 0
    node = grid[x][y]
    chk = [False] * 4
    for i in range(4):
        if chk[i]: continue
        chk[i] = True
        # 초기 방향
        init_dx = dx[i]
        init_dy = dy[i]
        distance = 0
        # 첫 이동 한다
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0:
            x = n - 1
        elif nx >= n - 1:
            x = 0
        else:
            x = nx
            
        if ny < 0:
            y = m - 1
        elif nx >= m - 1:
            y = 0
        else:
            y = ny
        
        distance += 1
                          
        # 이후 이동을 한다
        while True:
            # 이전 방향
            # dx[i], dy[i]
            # 현재 좌표
            # x, y
            # 새로운 방향 생성
            # S 일 때
            # if grid[x][y] == "S":
            #     pass
            # L 일 때
            if grid[x][y] == "L":
                if i == 0:
                    i = 3
                else:
                    i -= 1
            # R 일 때
            if grid[x][y] == "R":
                if i == 3:
                    i = 0
                else:
                    i += 1
            
            # 초기 좌표와 방향이 동일하면 빠져나옴
            if  x == 0 and y == 0:
                if init_dx == dx[i] and init_dy == dy[i]:
                    break
                else:
                    chk[i] = True
            
            # 새로운 좌표로 이동
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0:
                x = n - 1
            elif nx >= n:
                x = 0
            else:
                x = nx
                
            if ny < 0:
                y = m - 1
            elif nx >= m:
                y = 0
            else:
                y = ny
        
            # 거리 1 증가       
            distance += 1
            
        result.append(distance)
        
    

    return result



print(solution(["S"]))
# print(solution(["R","R"]))
# print(solution(["SL","LR"]))