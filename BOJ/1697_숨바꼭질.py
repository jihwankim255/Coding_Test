'''
BFS 라고 생각함. 최단거리이기 떄문에

아이디어
5를 기준으로 3가지 연산을 BFS로 탐색

chk: bool[] 을 만들어서 방문하지 않은 노드만 탐색

풀이: 실패
디버깅

'''
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, K = map(int, input().split())

limit = 100001
chk = [False] * limit
# 18개  0~17
def bfs(n, k):
  queue = deque()
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
      if (minus == k) or (plus == k) or (multiple == k):
        queue = []
        break
      if 0 <= minus <= limit and chk[minus] == False:
        queue.append(minus)
        chk[minus] = True
      if 0 <= plus <= limit and chk[plus] == False:
        queue.append(plus)
        chk[plus] = True
      if 0 <= multiple <= limit and chk[multiple] == False:
        queue.append(multiple)
        chk[multiple] = True
    

  return count

print(bfs(N, K))
# cont: 4
#  5    17
# chk = [ 3,4, 5,6,7,8,9 10,11,12,13, 14, 18,19, 20,21,22,24 ,40 ]
#  [                 14,   13,24,  18, 22    19,21,40   ]
'''
gpt의 풀이

<내 풀이와 비교>
n 값을 저장할 때 거리를 포함한 튜플을 큐에 넣으면 count 변수와 for문을 한번 덜쓸 수 있음.

MAX 값?


'''
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001
chk = [False] * MAX

def bfs(n, k):
    queue = deque()
    queue.append((n, 0))
    chk[n] = True

    while queue:
        v, count = queue.popleft()
        if v == k:
            return count
        for next_pos in (v - 1, v + 1, v * 2):
            if 0 <= next_pos < MAX and not chk[next_pos]:
                queue.append((next_pos, count + 1))
                chk[next_pos] = True

print(bfs(N, K))
