'''
큐에서 순서대로 넣고 꺼내면서 인접한 노드 중에 방문하지 않은 노드를 큐에 삽입
bfs 문제중에서도 쉬운 편이어서 실전에서 큰 도움이 안됨
'''

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end= ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
graph = [ [], [ 2, 4 ], [ 1, 4, 5 ], [], [ 1, 2, 5 ], [ 2, 4 ] ]
visited = [False] * 9
bfs(graph, 1, visited)






