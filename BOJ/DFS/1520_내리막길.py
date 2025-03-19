'''
for문을 돌면서
무한루프를 어떻게 막지?



'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

M, N = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1
    if dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            if (0 <= y + dy[i] < M and 0 <= x + dx[i] < N):
                if map[y][x] > map[y + dy[i]][x + dx[i]]:
                    dp[y][x] += dfs(y + dy[i], x + dx[i])
    return dp[y][x]


print(dfs(0, 0))