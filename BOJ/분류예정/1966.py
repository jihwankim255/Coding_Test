import sys
from collections import deque
input = sys.stdin.readline
n  = int(input())

for _ in range(n):
    N, M = map(int, (input().split()))
    queue = deque(map(int,input().split()))
    count = 0
    while queue:
        v = queue.popleft()
        maxv = 0
        if len(queue) > 0:
            maxv = max(queue)
        if v >= maxv:
            count += 1
            if M == 0:
                print(count)
                break
            else:
                M -= 1
        else:
            queue.append(v)
            if M == 0:
                M = len(queue) - 1
            else:
                M -= 1
# 1 1 1 1 1
# count: 3
# M: 3