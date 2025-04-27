'''
6명, [7,10]

7

'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
time = []
for _ in range(N):
    time.append(int(input()))
    
left = min(time)
right = max(time)* K
result = float('inf')

while left <= right:
    mid = (left+right)//2
    total = 0
    
    for i in time:
        total += mid // i
        
    if total >= K:
        right = mid - 1
        result = min(result, mid)
    else:
        left = mid + 1
        
print(result)