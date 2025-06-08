import sys
input = sys.stdin.readline

N = int(input())

TP = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]


'''
어려움
'''