'''
M미터 나무 필요
H미터 위로 올라감 0<=H
적어도 M미터 나무 얻기위한 H의 최댓값은?
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
ans = 0

while left <= right:
    mid = (left+right) // 2

    total = 0

    for tree in trees:
        if tree > mid:
            total += tree-mid

    if total >= M:
        # 나무가 너무 많이 잘렸으므로 높여야한다
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)