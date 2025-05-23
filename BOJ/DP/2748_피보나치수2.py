'''
n은 90이하 자연수
10

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
11개
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+2)]
dp[1] = 1

for i in range(n):
    dp[i+2] = dp[i] + dp[i+1]

print(dp[n])

'''
다른 사람 풀이
n = 10 일때
2이상 10이하
0, 1->1,1->1,2

a,b = b, a+b

'''

def fibo(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b= b, a + b
    return b


'''
풀이2
내풀이는 i=0부터 계산했지만 그러면 10번 연산을 하므로
index out of range 에러가뜸
dp[1]은 이미 주어졌으므로 9번만 연산하면 됨
'''
N=int(input())
fibo=[0]*(N+1)
fibo[0]=0
fibo[1]=1
for i in range(2,N+1):
    fibo[i]=fibo[i-1]+fibo[i-2]
print(fibo[N])