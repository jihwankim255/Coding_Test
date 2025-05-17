'''
https://www.youtube.com/watch?v=AjFlp951nz0

2개의 힙 아이디어를 생각하긴했는데 어떻게 동기화하는 부분이 생각이 안나서 버렸음
하나의 힙에서 처리하려고만 생각함

'''

import sys
input = sys.stdin.readline
from collections import deque
from heapq import heapify, heappop, heappush

T = int(input())

for i in range(T):
    minHeap, maxHeap = [], []
    k = int(input())
    visited = [False] * k
    for _ in range(k):
        di, n = input().split()
        n = int(n)
        if di == 'I':
            heappush(minHeap, (n, i))
            heappush(maxHeap, (-n, i))
            visited[i] = True
        elif di == 'D':
            if n == 1:
                while maxHeap and not visited[maxHeap[0][1]]:
                    heappop(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][1]] = False
                    heappop(maxHeap)
            elif n == -1:
                while minHeap and not visited[minHeap[0][1]]:
                    heappop(minHeap)
                if minHeap:
                    visited[minHeap[0][1]] = False
                    heappop(minHeap)
    while minHeap and not visited[minHeap[0][1]]:
        heappop(minHeap)
    while maxHeap and not visited[maxHeap[0][1]]:
        heappop(maxHeap)
    if not minHeap or not maxHeap:
        print("EMPTY")
    else:
        print(-maxHeap[0][0], minHeap[0][0])