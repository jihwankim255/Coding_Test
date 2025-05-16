'''
BFS로 판단
'''

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
chk = [False] * 10000
def D(A):
    A
    return
def S(A):
    return
def L(A):
    return
def R():
    return

# '1234'
for _ in range(T):
    A, B =  list(input().split())
    Q = deque()
    Q.append((A, 0))

    while Q:
        v, count = Q.popleft()
        d = D(v)
        s = S(v)
        l = L(v)
        r = R(v)




def BFS():
    return

print(BFS())