'''
안전영역 최대 크기
여기 라는걸 어떻게 알지?
3 ≤ N, M ≤ 8

최대 8 x 8 = 64칸
중에 3개니까
64C3
64 63 62
'''
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

dy = [1,0,-1,0]
dx = [0,1,0,-1]

graph = []
rooms = []
viruses = []

for j in range(N):
    temp = list(map(int,input().split()))
    graph.append(temp)
    for i, val in enumerate(temp):
        if val == 0:
            rooms.append((j, i))
        elif val == 2:
            viruses.append((j, i))

room_len = len(rooms)
max_safe = 0

def spread_virus():
    """바이러스를 확산시키고 확산된 맵을 반환"""
    temp_graph = [row[:] for row in graph]  # 깊은 복사
    queue = deque(viruses)
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < M:
                if temp_graph[ny][nx] == 0:
                    temp_graph[ny][nx] = 2
                    queue.append((ny, nx))
    
    return temp_graph

def count_safe_area(temp_graph):
    """안전 영역의 개수를 세는 함수"""
    count = 0
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                count += 1
    return count
# 모든 0 중에서 3개를 뽑는 경우의 수
for i in range(room_len):
    for j in range(i+1, room_len):
        for k in range(j+1, room_len):
            # 해당 방에 벽을 세운다
            graph[rooms[i][0]][rooms[i][1]] = 1
            graph[rooms[j][0]][rooms[j][1]] = 1
            graph[rooms[k][0]][rooms[k][1]] = 1
            
            # 바이러스 확산 시뮬레이션
            infected_graph = spread_virus()
            
            # 안전 영역 계산
            safe_count = count_safe_area(infected_graph)
            max_safe = max(max_safe, safe_count)
            
            # 다시 원래대로 복구
            graph[rooms[i][0]][rooms[i][1]] = 0
            graph[rooms[j][0]][rooms[j][1]] = 0
            graph[rooms[k][0]][rooms[k][1]] = 0

print(max_safe)