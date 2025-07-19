'''
그냥 구현문제로 느껴짐
처음에 단순 for문으로 구현
다리 위의 무게를 매번 추적해야 하기 때문에 실제로 queue를 만들어서 관리해야함
'''
import sys
input  = sys.stdin.readline
from collections import deque
n, w, L = map(int, input().split())

trucks = deque(map(int,input().split()))

timer = 0

# 최대 하중 만큼 담을수 있는 큐를 만든다 -> 굳이 만들어야하나? -> 무게를 실시간으로 알야야하기 때문

total = deque([0 for _ in range(w)])
total_w = 0
total_len = 0

while trucks or sum(total) > 0:
    timer += 1

    total.popleft()
    if trucks:
        if sum(total) + trucks[0] <= L:
            total.append(trucks.popleft())
        else:
            total.append(0)
print(timer)
