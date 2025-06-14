'''
아이디어
서류를 기준으로 오름차순 정렬을 한다.
그러면, 하나씩 탐색할 때, 면접점수는 무조건 이전 최소 면접점수보다 낮아야 합격한다.
정렬을 하면
1 2 3 4 5 6 7
4 5 6 2 7 1 3
와 같은데, for문을 돌리면
1은 무조건 합격
2는 이전 최소인 4등보다 아래이므로 불합격. (1,4)가 (2,5)의 상위호환
(3,6)은 마찬가지로 4등보다 아래이므로 불합격
(4,2)는 이전 최소인 4보다 높으므로 합격. 최소 면접점수를 2로 갱신
반복.... 
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cnt = 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    
    cnt = 1
    min_v = arr[0][1]
    for i in range(N):
        if arr[i][1] < min_v:
            cnt += 1
        min_v = min(min_v, arr[i][1])
            
    print(cnt)
'''
다른 풀이
내 풀이와 다른 점은, 나는 min을 써서 이전 값보다 작은지 비교를 했다.
근데 이전최소(min_v)보다 arr[i][1]가 작기만하면 그게 최소값이 되기 때문에 min을 안써도 된다.
내 풀이에서 min_v = min(min_v, arr[i][1]) 를 min_v = arr[i][1]로 바꾸고 위의 if문에 넣으면 됨
'''
    
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    top = 0
    result = 1
    
    for i in range(1, len(rank_asc)):
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            result += 1
    
    print(result)