import sys
from collections import deque
input = sys.stdin.readline
from heapq import heappush, heappop
'''
내 풀이
넣을때 양수는 1 음수는 -1 과 함께 넣는다
다른 풀이
넣을때 (abs(num), num) 으로 절댓값과 원래값을 함께 넣는다.
튜플을첫번째 수로 정렬이 되어 들어가고 출력은 원래값을 한다.
'''

N = int(input())
absHeap = []
for _ in range(N):
    x = int(input())
    if x != 0:
        if x > 0:
            heappush(absHeap, (x, 1))
        else:
            heappush(absHeap, (-x, -1))
    else:
        if len(absHeap) == 0:
            print(0)
        else:
            ans, pm = heappop(absHeap)
            if pm == 1:
                print(ans)
            else:
                print(-ans)