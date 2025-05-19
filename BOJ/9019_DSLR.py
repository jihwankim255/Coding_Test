'''
BFS로 판단
문제를 제대로 읽지 않아서 틀렸다.
L,R에서 10에대해 실행하면 01이 돼서 1이 되는줄 알았는데 100이 돼야한다.
'''

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def D(A):
    res = A * 2
    if res > 9999:
        return res % 10000
    return res
def S(A):
    if A == 0:
        return 9999
    return A - 1
def L(n):
    return (n % 1000) * 10 + (n // 1000)

def R(n):
    return (n % 10) * 1000 + (n // 10)


for _ in range(T):
    chk = [False] * 10001
    A, B =  list(map(int,input().split()))
    Q = deque()
    Q.append((A, ''))
    chk[A] = True

    while Q:
        v, count = Q.popleft()
        d = D(v)
        s = S(v)
        l = L(v)
        r = R(v)
        if d == B:
            print(count+'D')
            break
        if s == B:
            print(count+'S')
            break
        if l == B:
            print(count+'L')
            break
        if r == B:
            print(count+'R')
            break
        if chk[d] == False:
            Q.append((d, count+'D'))
            chk[d] = True
        if chk[s] == False:
            Q.append((s, count+'S'))
            chk[s] = True
        if chk[l] == False:
            Q.append((l, count+'L'))
            chk[l] = True
        if chk[r] == False:
            Q.append((r, count+'R'))
            chk[r] = True
