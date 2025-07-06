import sys
input = sys.stdin.readline

# todo 0이면 이미 최소이므로 비교할 필요없이 바로 종료

# 아래, 위, 오른쪽, 왼쪽
dir = [(1,0),(-1,0),(0,1),(0,-1)]

N, M = map(int, input().split())

graph = []
cctv_arr = []  # [(1, 1, 2), (3, 4, 2), (5, 5, 5)]
sagakjidae = 0 # 0의 개수 
max_safe = 0


# cctv 각 케이스
temp = []

for j in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for i in range(M):
        v = arr[i]
        if v == 0:
            sagakjidae += 1
        elif v != 6:
            cctv_arr.append((j, i, v))

# 방향과 타입이 주어지면 for문 돌면서 graph에서 safe count 1씩 증가 최대값 갱신

def count_sagak(temp):
    safe_count = 0
    for t_dir, num in temp:  # number, number
        n = 1
        while True:
            ny = j + dir[t_dir][0] * n
            nx = i + dir[t_dir][1] * n
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == 0:
                    safe_count += 1
                    graph[ny][nx] = -1
                    n += 1
                elif graph[ny][nx] == 6:
                    break
            else:
                break
    global max_safe   
    max_safe = max(max_safe, sagakjidae - safe_count)             
                

# 각 CCTV의 모든 경우의 수에 대해 카운트 해야하므로 백트래킹
def recur(num):
    if num == len(cctv_arr):
        print('@ ', temp)
        # 사각지대 계산
        count_sagak(temp)
        #최소값과 비교
        return
    if cctv_arr[num][2] == 1:
        for i in range(4):
            temp.append((i,num))
            recur(num+1)
            temp.pop()
    if cctv_arr[num][2] == 2:
        for i in [0, 2]:
            temp.append((i,num))
            recur(num+1)
            temp.pop()
    if cctv_arr[num][2] == 3:
        for i in range(4):
            temp.append((i,num))
            recur(num+1)
            temp.pop()
    if cctv_arr[num][2] == 4:
        for i in range(4):
            temp.append((i,num))
            recur(num+1)
            temp.pop()
    if cctv_arr[num][2] == 5:
        temp.append((0, num))
        recur(num+1)
        temp.pop()
    
recur(0)

print('ans: ', max_safe)
# 모든 경우의 수를 배열에 담음 -> 시간초과날수있음
# for ey, ex, type in cctv_arr:
#     print("ey, ex, type: ",ey, ex, type)
#     if type == 1:
#         temp.append()



# 각 경우의 수에 대해 사각지대의 수를 구하고 최소를 갱신
