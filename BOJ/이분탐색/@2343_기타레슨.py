'''
N개를 M개로 나누기
M개는 모두 같은 크기여야 함
이분탐색
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0
left, right = max(arr), sum(arr)

while left <= right:
    mid = (left+right) // 2
    
    # 블루레이에 강의 넣기
    count, sum = 0, 0
    for i in range(N):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]
    if sum:
        count += 1
        
    if count > M:
        left = mid + 1
    else:
        right = mid -1
        ans = mid

print(ans)
