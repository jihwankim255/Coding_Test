# n = input()
# arr = [list(map(int, input().split())) for _ in range(n-1)]

# print("n은: ", n)
# print("arr은: ", arr)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def is_interval_graph(n, edges):
    adjacency_list = [[] for _ in range(n)]
    
    for edge in edges:
        u, v = edge
        adjacency_list[u - 1].append(v)
        adjacency_list[v - 1].append(u)
  
    intervals = [None] * n
    visited = [False] * n
    
    def dfs(node, parent, left, right):
        if visited[node]:
            return True
        
        visited[node] = True
        intervals[node] = (left, right)
        
        for child in adjacency_list[node]:
            if child == parent:
                continue
            if not dfs(child, node, left - 1, right + 1):
                return False
        return True
    
    if not dfs(0, -1, float('-inf'), float('inf')):
        return -1
    
    return intervals

# 입력 받기
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]

# 판별 및 출력
intervals = is_interval_graph(n, edges)
if intervals == -1:
    print(-1)
else:
    print(1)
    for i in range(1, n):
        print(intervals[i][0], intervals[i][1])



'''
3
3 2
1 2

6
4 1
3 1
2 1
5 1
5 6

7
1 2
2 3
1 4
4 5
1 7
6 7


'''