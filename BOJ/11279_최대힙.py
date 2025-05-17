import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input().strip())

heap = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            ans = heappop(heap)
            print(-ans)
    else:
        heappush(heap, -x)