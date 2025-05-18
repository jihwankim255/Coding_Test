import sys
input = sys.stdin.readline
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
graphMax = [[0,0,0] for _ in range(N + 1)]
graphMin = [[0,0,0] for _ in range(N + 1)]

def DFS(N):
    if N == 1:
        graphMax[1] = graph[0]
        graphMin[1] = graph[0]
        return
    DFS(N-1)
    if max(graphMax[N-1]) == graphMax[N-1][0]:
        graphMax[N][0] = graphMax[N-1][0] + graph[N-1][0]
        graphMax[N][1] = graphMax[N-1][0] + graph[N-1][1]
        graphMax[N][2] = max(graphMax[N-1][1],graphMax[N-1][2]) + graph[N-1][2]
        
        graphMin[N][0] = graphMin[N-1][1] + graph[N-1][0]
        graphMin[N][1] = min(graphMin[N-1][1],graphMin[N-1][2]) + graph[N-1][1]
        graphMin[N][2] = min(graphMin[N-1][1],graphMin[N-1][2]) + graph[N-1][2]
    elif max(graphMax[N-1]) == graphMax[N-1][1]:
        graphMax[N][0] = graphMax[N-1][1] + graph[N-1][0]
        graphMax[N][1] = graphMax[N-1][1] + graph[N-1][1]
        graphMax[N][2] = graphMax[N-1][1] + graph[N-1][2]
        
        graphMin[N][0] = graphMin[N-1][0] + graph[N-1][0]
        graphMin[N][1] = min(graphMin[N-1][0],graphMin[N-1][2]) + graph[N-1][1]
        graphMin[N][2] = graphMin[N-1][2] + graph[N-1][2]
    else:
        graphMax[N][0] = max(graphMax[N-1][0],graphMax[N-1][1]) + graph[N-1][0]
        graphMax[N][1] = graphMax[N-1][2] + graph[N-1][1]
        graphMax[N][2] = graphMax[N-1][2] + graph[N-1][2]
        
        graphMin[N][0] = min(graphMin[N-1][0],graphMin[N-1][1]) + graph[N-1][0]
        graphMin[N][1] = min(graphMin[N-1][0],graphMin[N-1][1]) + graph[N-1][1]
        graphMin[N][2] = graphMin[N-1][1] + graph[N-1][2]

DFS(N)
print(max(graphMax[N]), min(graphMin[N]))
    