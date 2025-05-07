# BFS 라고 생각함. 최단거리이기 떄문에
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, K = map(int, input().split())

chk = [False] * 100001
# 18개  0~17
def bfs(n, k):
  queue = deque([])
  count = 0
  queue.append(n)
  chk[n] = True
  
  while queue:
    count += 1
    for _ in range(len(queue)):
      v = queue.popleft()
      minus = v - 1
      plus = v + 1
      multiple = 2 * v
      if 0 <= minus <= 100000 and chk[minus] == False:
        queue.append(minus)
        chk[minus] = True
      if 0 <= plus <= 100000 and chk[plus] == False:
        queue.append(plus)
        chk[plus] = True
      if 0 <= multiple <= 100000 and chk[multiple] == False:
        queue.append(multiple)
        chk[multiple] = True
    if (minus is k) or (plus is k) or (multiple is k):
        break

  return count

print(bfs(N, K))
# cont: 4
#  5    17
# chk = [ 3,4, 5,6,7,8,9 10,11,12,13, 14, 18,19, 20,21,22,24 ,40 ]
#  [                 14,   13,24,  18, 22    19,21,40   ]
