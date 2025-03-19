'''



N까지 M개 고른 수열
중복 허용




'''
import sys
input = sys.stdin.readline

N, M =  map(int, input().split())
rs = []

def recur(start):
    if len(rs) == M:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(start, N+1):
        rs.append(i)
        recur(i)
        rs.pop()



recur(1)

'''
1 2 3 4
1 

4 2

1 1
1 2
1 3
1 4
2 2
2 3
2 4
'''