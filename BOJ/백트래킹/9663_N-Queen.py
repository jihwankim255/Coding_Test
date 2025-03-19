'''

아이디어
이게 백트래킹인지 어떻게암?

시간복잡도


자료구조

2-2개
10 01
01 10

3-6 개         3p2   
100            1      2       3
010 001       2 3    1  3   2   3 
011 

4-24 개       1  2 3 4 개  4p3
0100             1             2        3         4
0001          2   3   4    1  3   4   1  2 4   1  2  3                                      
1000       3   4  
0010
                  1 
5    5p4   54321 120개?
한행에 하나
한열에 하나

'''


import sys
input = sys.stdin.readline

N = int(input())
	
visited = [0] * N
cnt = 0

def check(now_row):
    for row in range(now_row):
        if visited[now_row] == visited[row] or now_row - row == abs(visited[now_row] - visited[row]):
            return False
    return True

def dfs(row):
    global cnt
    
    if row == N: 
        cnt += 1

    else:
        for col in range(N):
            visited[row] = col
            if check(row): 
                dfs(row + 1) 
                
dfs(0)
print(cnt)