import sys
input = sys.stdin.readline


map = [
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0], 
    [0, 0, 0, 0, 0], 
    [1, 0, 1, 1, 1], 
    [0, 0, 1, 1, 1], 
    [0, 0, 1, 1, 1]
]

# 4 9
def solution(map):
    row = len(map)
    col = len(map[0])
    chk = [[False] * col for _ in range(row)]
    count = 0
    maximum = 0
    
    for i in range(row):
        for j in range(col):
            if map[i][j] == 1 and chk[i][j] == False:
                chk[i][j] = True
                count += 1
                maximum = max(maximum, bfs(i, j, map, chk))
    
    
    return count, maximum
    
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x, y, map, chk):
    result = 1
    queue = [(x, y)]
    
    while queue:
        ex, ey = queue.pop()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] == 1 and chk[nx][ny] == False:
                result += 1
                chk[nx][ny] = True
                queue.append((nx, ny))
                               
    return result
    
    


print(solution(map))




import sys
input = sys.stdin.readline
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

count = 0
maximum = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

                               

for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            count += 1
            maximum = max(maximum, bfs(i, j, map, chk))

def bfs(x, y, map, chk):
    result = 1
    queue = [(x, y)]
    
    while queue:
        ex, ey = queue.pop()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] == 1 and chk[nx][ny] == False:
                result += 1
                chk[nx][ny] = True
                queue.append((nx, ny))
    return result
                
print(count)
print(maximum)