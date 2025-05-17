'''
BFS?
그리디?
뒤로 가야 좋은 경우가 있나?

30~
1~6까지는 이동가능 1번으로 침

1-> 50이라고 치자

3~48 사다리가 있으면

1->3 3~48 48->50 3번 가능

이전에 그리디 문제를 풀어서 그리디 문제인줄 알았는데 BFS문제였음
그리디가 성립하지 않는 이유를 찾을수 있어야함
그리디는 선택지 중에 현재 최선 = 전체 최선을 만족해야 한다
회의실 문제에서는 선택 대상이 회의 였지만
이 문제에서 선택 대상은 1~6 주사위이다. 따라서 항상 6을 선택하는게 최선이 아닌 3을 선택해도
6보다 좋은 결과가 나올수 있기 때문에 그리디로 풀 수 없다.

'''


import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

current = 1
visited = [False] * 101
keys = []
values = []
for i in range(N+M):
    k, v = map(int, input().split())
    keys.append(k)
    values.append(v)


def BFS():
    q = deque()
    q.append((current, 0))
    visited[current] = True
    while q:
        cur, count = q.popleft()
        # 주사위 굴리기
        for i in range(6):
            new_cur = cur + i + 1
            if new_cur >= 100:
                return count + 1
            if visited[new_cur] == False:
                visited[new_cur] = True
                for idx, k in enumerate(keys):
                    if k == new_cur:
                        new_cur = values[idx]
                        visited[new_cur] = True
                        break
                q.append((new_cur, count + 1))

print(BFS())


'''
나는 리스트 2개를 만들어서 사용했는데
대부분은 딕셔너리 하나로 구현했다.
리스트 2개는 헷갈려서 실수를 유발하기 때문에 딕셔너리 방식이 나은 것 같다.

'''