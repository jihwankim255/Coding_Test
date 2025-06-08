import sys
input = sys.stdin.readline

n = int(input())


a_count = 0
b_count = 0

def solution(n):
    a = [1, 0]
    b = [0, 1]
    if n == 1:
        return a
    elif n == 2:
        return b
    
    for i in range(2, n):
        a, b = b, [a[0]+b[0], a[1]+b[1]]
    return b

ans = solution(n+1)

print(str(ans[0]),str( ans[1]))
