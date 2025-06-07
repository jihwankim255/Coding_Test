import sys
input = sys.stdin.readline

n = int(input())   

arr = []

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    
dp = [arr[0]]
for i in range(1, len(arr)):
    temp = []
    for idx, j in enumerate(arr[i]):
        if idx == 0:
            temp.append(dp[i-1][0] + arr[i][0])
        elif idx == i:
            temp.append(dp[i-1][i-1] + arr[i][i])
        else:
            temp.append(max(dp[i-1][idx-1],dp[i-1][idx])+arr[i][idx])
    dp.append(temp)
    

print(max(dp[-1]))
'''

'''