import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# res = 10**10

# def getScore(arg):
#     score = 0
#     com = list(combinations(list(arg), 2))
#     for a, b in com:
#         score += arr[a-1][b-1] + arr[b-1][a-1]
    
#     return score

# pre_cases = list(combinations([i+1 for i in range(N)], N//2))
# pre_cases_len = len(pre_cases)

# for i in range(0,len(pre_cases)//2):
#     team_a = pre_cases[i]
#     team_b = pre_cases[pre_cases_len - i - 1]
#     res = min(res, abs(getScore(team_a) - getScore(team_b)))

# print(res)

'''
경우의 수를 모두 구함
조합으로 품

# 다른 풀이
백트래킹: 가능한 모든 경우.
n: 사람 번호
https://www.youtube.com/watch?v=vOqtJotB5Ps

'''
def cal(alist, blist):
    asm = bsm = 0
    for i in range(M):
        for j in range(M):
            asm += arr[alist[i]][alist[j]]
            bsm += arr[blist[i]][blist[j]]
    return abs(asm - bsm)

def dfs(n, alist, blist):
    global ans
    if ans == 0: return
    if n ==N:
        if len(alist) == len(blist):
            ans = min(ans, cal(alist, blist))
        return
    
    dfs(n+1, alist+[n], blist) # A팀 선택
    dfs(n+1, alist, blist+[n]) # B팀 선택

M = N//2

ans = 100*M*M
dfs(0, [], [])
print(ans)