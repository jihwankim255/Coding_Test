'''

0층  1  2   3  4  5
1층  1  3   6  10  15
2층  1  4   10  20  35
3층  1  5  15  35  70
4층
k  n
2, 3
[
   [0, 1, 2, 3], 
   [0, 1, 3, 0], 
   [0, 0, 0, 0], 
   [0, 0, 0, 0]
]
dp:  [
    [0, 1, 2, 3], 
    [0, 1, 3, 6], 
    [0, 0, 0, 0], [0, 0, 0, 0]]
    
층을 k개를 만들어야 하는데 n개를 만들어서 틀림
'''

import sys
input = sys.stdin.readline

T = int(input())

def getDP(k, n,dp):
    for j in range(1,k+1):
        for i in range(1,n+1):
            dp[j][i] = dp[j-1][i] + dp[j][i-1]
    
    return dp[k][n]


for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [[i for i in range(n+1)]] + [ [0]*(n+1) for _ in range(k)]
    print(getDP(k,n,dp))
    
    
'''
@다른 풀이 1
한 층에 덮어 씌우는 방식
@내 풀이
모든 층을 구하는 방식


'''
# t = int(input())

# for _ in range(t):  
#     floor = int(input()) 
#     num = int(input())  
#     f0 = [x for x in range(1, num+1)]  
#     for k in range(floor):  
#         for i in range(1, num):  
#             f0[i] += f0[i-1] 
#     print(f0[-1])

'''
다른 풀이 2
'''
t = int(input())

for i in range(t):
    k = int(input())        # 층
    n = int(input())        # 호
    people = [i for i in range(1, n+1)]     # 0층

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y+1]))   # 아래층의 1~n호 까지의 합
        people = new.copy()
        #print(people)		# peaple에 들어있는 값 출력해 봄
    print(people[-1])       # K층 n호
