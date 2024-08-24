def my_solution(n, results):
    answer = 0
    # [[1,5],[1,5],[1,5],[1,5],[1,5]]
    players = [[1,5] for _ in range(n)]    
    
    for result in results:
        winner = players[result[0] - 1]
        loser = players[result[1] - 1]
        # 승자의 최대값 감소
        if winner[0] < winner[1]:
            winner[1] = min(winner[1] - 1, loser[1] - 1)
        # 패자의 최소값 증가
        if loser[0] < loser[1]:
            loser[0] = max(winner[0] + 1, loser[0] + 1)
    return players
# print(my_solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# 4    3 
#      2
     
#     [2, 4]  [3, 5]

from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results: 
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])
        
    for i in range(1, n + 1):
        for winner in lose[i]: 
            win[winner].update(win[i])
        for loser in win[i]: 
            lose[loser].update(lose[i])
        
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


def solution2(n, results):
    total = [['?' for i in range(n)] for j in range(n)]

    for i in range(n):
        total[i][i] = 'SELF'

    for result in results:
        total[result[0]-1][result[1]-1] = 'WIN'
        total[result[1]-1][result[0]-1] = 'LOSE'

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'WIN' and total[k][j] == 'WIN':
                    total[i][j] = 'WIN'
                elif total[i][k] == 'LOSE' and total[k][j] == 'LOSE':
                    total[i][j] = 'LOSE'

    answer = 0

    for i in total:
        if '?' not in i:
            answer += 1

    return answer

print(solution2(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


from collections import defaultdict

def solution(n, results):
    win = defaultdict(set)
    lose = defaultdict(set)
    for i in results:
        win[i[0]].add(i[1])
        lose[i[1]].add(i[0])
    answer = 0
    for i in range(1, n+1):
        if bfs(win ,i) + bfs(lose, i) == n-1:
            answer += 1
    return answer

def bfs(graph, start):
    queue = [[start, 0]]
    visited = []
    a = -1
    while queue:
        current = queue.pop(0)
        if current[0] not in visited:
            a += 1
            visited.append(current[0])
            if current[0] in graph:
                win = set(graph[current[0]]) - set(visited)
                queue.extend([[i, current[1]+1] for i in win])
    return a
        