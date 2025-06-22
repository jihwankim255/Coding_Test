# import sys
# input =sys.stdin.readline

# N, M = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(N)]


def combinations(s, n, r):
    arr = []
    for i in range(s, n-r):
        combinations(s+1, n ,r-1)
    
    
    return arr

combinations(1, 5, 3)
'''
치킨집이 5개있어
3개만 남긴대
어떤 3개임? 다 확인해야지?
1,2,3,4,5
이중에 3개만 선택하는 경우의 수




치킨집을 폐점시킨다.



치킨거리를 계산한다

'''