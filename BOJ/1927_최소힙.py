import sys
import heapq
input = sys.stdin.readline

heap = []

N = int(input())
for _ in range(N):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, x)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))