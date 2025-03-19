'''
N-Queen 연습

'''

import sys
input = sys.stdin.readline
N = int(input())

chk = [0] * N
ans = 0

def check(now_row):
    for i in range(now_row):
        if chk[now_row]== chk[i] or now_row-i == abs(chk[now_row]-chk[i]):
            return False
    return True
def dfs(row):
    global ans
    if row == N:
        ans += 1
    else:
        for i in range(N):
            chk[row] = i   
            if check(row):
                dfs(row+1)     


dfs(0)
print(ans)