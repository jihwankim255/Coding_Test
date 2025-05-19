def solution(triangle):
    dp = [triangle[0]] + [[0] * len(triangle[i]) for i in range(1, len(triangle))]
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            if dp[i + 1][j] < dp[i][j] + triangle[i+1][j]:
                dp[i + 1][j] = dp[i][j] + triangle[i+1][j]
            if dp[i+1][j+1] < dp[i][j] + triangle[i+1][j+1]:
                dp[i+1][j+1] = dp[i][j] + triangle[i+1][j+1]
    return dp


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

