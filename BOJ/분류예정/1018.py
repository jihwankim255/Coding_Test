import sys
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(input().strip()) for _ in range(N)]
chess = [['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B']]

repaint = 64
answer = 64
# 01맵 만들기
for j in range(N-7):
    for i in range(M-7):
        count = 0
        for row in range(8):
            for col in range(8):
                if map[j+row][i+col] != chess[row][col]:
                    count += 1
        answer = min(answer,min(count, repaint-count))
print(answer)