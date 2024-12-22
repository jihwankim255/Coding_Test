'''
hf"t: {T}"tps://www.acmicpc.net/problem/1012
dfs
테스트케이스가 머임?


'''

# n, m = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(m)]

T = input()
print(f"T: {T}")

for i in T:
    M, N, K = map(int, input().split())
    print(f"M: {M}, N: {N}, K: {K}")
    for j in K:
        x, y = map(int, input().split())
        print(f"x: {x}, y: {y}")