def solution(land):
    answer = 0
    dp = [land[0]] + [[0,0,0,0] for i in  range(1, len(land))]
    # 4열 만큼 실행
    # for k in range(4):
        # 행
    for i in range(1, len(land)):
        # 열
        for j in range(4):
            maxn = 0
            for k in range(4):
                if k != j and maxn < dp[i-1][k]:
                    dp[i][j] = land[i][j] + dp[i-1][k]
                    maxn = dp[i-1][k]
    return max(dp[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
# dp = [[1, 2, 3, 5], [10, 11, 12, 11], [16, 15, 13, 13]]
# print(max(dp[-1]))