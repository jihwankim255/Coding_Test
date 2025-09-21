'''
공유기 최대거리를 정한다음
이게 맞는지 어떻게 확인하지?
이분탐색 + 그리디
집이 정렬돼 있고, 왼쪽부터 설치하면 최대한 많은 공유기를 가장 간격 넒게 설치 가능
모든 조합을 찾는 문제가 아님

while 문 내부의 count와 C를 비교
'''


import sys
input = sys.stdin.readline

N, C = map(int, input().split()) 

arr = [int(input().strip()) for _ in range(N)]

arr.sort()

left = 1
right = max(arr)
ans = 0

while left <= right:
    mid = (left + right) // 2
    # 현재에 저장된 값과 비교하기
    current = arr[0]
    count = 1
    
    for i in range(1, N):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]
    if count >= C:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
        
print(ans)
        
                
    