'''
아이디어
arr
0 10 20 10 30 20 50
dp
0 1 2 1 3 2 4
dp: i번째 숫자를 포함했을 때 최대 길이
dp[i] = dp[0]~dp[i-1] 중 최대값 + 1
(arr[i]>arr[j] 인 경우 중에서)
dp[0] = 0
for i (1,N+1):
  mx = 0
  for j (0, i):
    if arr[i]>arr[j]:
      mx = max(mx, dp[j])
dp[i] = mx + 1
'''

import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

dp = [0] * N

for i in range(N):
      mx = 0
      for j in range(i):
            if arr[i] > arr[j]:
                  mx = max(mx, dp[j])
      dp[i] = mx + 1
      
print(max(dp))
'''
다른 풀이 (이진탐색)
여기에서 dp는 실제 lis와 다름
ex) 20 30 10
실제는 [20, 30]이지만 이진탐색 결과는 [10, 30]이 됨
lis를 구하는 방식이 아니라 dp의 마지막 요소에 기존 수열보다 작은 값으로
끝나는 수열을 만드는 방식

'''
N = int(input())  
arr = list(map(int, input().split()))  
import bisect

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

dp = [arr[0]]
for i in range(1, N):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        index = binary_search(dp, arr[i])
        dp[index] = arr[i]
print(len(dp))
