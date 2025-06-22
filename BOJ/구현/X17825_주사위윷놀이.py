import sys
input = sys.stdin.readline
from collections import deque

score = 0

numbers = list(map(int, input().split()))

# 말의 위치, 점수
p_1 = (0, 0)
p_2 = (0, 0)
p_3 = (0, 0)
p_4 = (0, 0)

# 윷놀이 판과 점수
arr_1 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40] # 2~40 전체
arr_2 = [10,13,16,19,25,30,35,40] # 10~40
arr_3 = [20,22,24,25,30,35,40] # 20~40
arr_4 = [30,28,27,26,25,30,35,40] # 30~40

