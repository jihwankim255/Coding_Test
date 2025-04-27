import sys
import pprint
input =sys.stdin.readline
N,M = map(int,input().split())
map = [list(input().strip()) for _ in  range(N)]
print('==========')
pprint.pprint(map)