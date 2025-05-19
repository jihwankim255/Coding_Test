def solution(x, y):
    if x<= -1 or x>= n or y <= -1 or y >=m:
        return False
    if graph[x][y] ==0:
        graph[x][y] = 1
        solution(x -1, y)
        solution(x, y - 1)
        solution(x + 1, y)
        solution(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if solution(i, j) == True:
            result += 1
            
print(result)
'''
4 5
00110
00011
11111
00000
출력: 3
'''