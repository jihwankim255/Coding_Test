
import sys
input = sys.stdin.readline
import heapq

N = int(input())

arr = [int(input()) for
       _ in range(N)]

total_cost = 0

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    sum_v = a + b
    
    total_cost += sum_v
    heapq.heappush(arr, sum_v)
    
print(total_cost)


N = int(input())

arr = []
for i in range(N):
    heapq.heappush(arr, int(sys.stdin.readline()))
total_cost = 0

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    sum_v = a + b
    
    total_cost += sum_v
    heapq.heappush(arr, sum_v)
    
print(total_cost)
