'''
그리디 문제라는 것을 알 수 없었음
문제풀이 양이 부족
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

arr = [tuple(map(int, input().split()))for _ in range(N)]
arr.sort(key=lambda x:(x[1], x[0]))
end = arr[0][1]
count = 1
for i in range(1, N):
    if end <= arr[i][0]:
        end = arr[i][1]
        count += 1
print(count)

'''
1 4
5 7
8 11
12 14

'''