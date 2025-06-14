import sys
input = sys.stdin.readline

# N = int(input())
# arr = list(map(int,input().split()))
# idx_arr = [i for i in range(N)]

# result = [0 for _ in range(N)]


# for i in range(N):
#     result[idx_arr[arr[i]]] = i+1
#     del idx_arr[arr[i]]

# print(' '.join(map(str,result)))

'''
다른 풀이
내풀이는 idx배열을 따로 만들어서 사용한 인덱스를 제거하는 방식을 썼다.
다른풀이는 배열을 만들지 않는 대신, for문을 한번 더 체크해서 0의 수를 카운트

'''
import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
result = [0]*(n)

for i in range(n):
    cnt = 0
    for j in range(n):
        if result[j] == 0:
            cnt += 1
        if cnt == heights[i]+1:
            result[j] = i+1
            break


print(*result)
