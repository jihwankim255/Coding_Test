import sys
input = sys.stdin.readline
import copy

N = int(input())
arr = list(map(int, input().split()))
add, minus, multi, divi = map(int, input().split())
caculators = []
for i in range(add):
    caculators.append('+')
for i in range(minus):
    caculators.append('-')
for i in range(multi):
    caculators.append('*')
for i in range(divi):
    caculators.append('/')
chk = [False] * N  # 6개

rs = []
temp = []
def recur(num):
    if num == (N-1):
        copied = copy.deepcopy(temp)
        rs.append(copied)
        return
    for i in range(N-1):   # 0, 4
        if chk[i] == False:
            chk[i] = True
            temp.append(caculators[i])
            recur(num+1)
            chk[i] = False
            temp.pop()

recur(0)
# print(rs)
def calculate(num1, num2, calculator):
    if calculator == '+':
        return num1 + num2
    elif calculator == '-':
        return num1 - num2
    elif calculator == '*':
        return num1 * num2
    elif calculator == '/':
        if num1 < 0:
            return -(abs(num1) // num2)
        else:
            return num1 // num2

for idx, r in enumerate(rs):
    temp = arr[0]
    for i in range(1,N):
        temp = calculate(temp, arr[i], r[i-1])
    rs[idx] = temp

print(max(rs))
print(min(rs))
        


'''
+ + - * /


연산자 경우의수만 알면
계산 하고 최대값 최솟값을 구하면됨

필터하는법 공부해야함
'''
'''
다른 풀이
내 풀이처럼 굳이 연산자를 문자열로 바꾸지 않고
연산자 개수에서 1개씩 차감하는 방식으로 함
'''
N = int(input())

lst = list(map(int, input().split()))

operators = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(n, temp) :
    global mx, mn
    
    # 종료 조건
    if n == N-1:
        mx = max(temp, mx)
        mn = min(temp, mn)
        return
     
    # 하부함수 호출
    if operators[0] != 0 : # 덧셈하는 경우
        operators[0] -= 1
        dfs(n+1, temp + lst[n+1])
        operators[0] += 1 

    if operators[1] != 0 : # 뺄셈하는 경우
        operators[1]-= 1
        dfs(n+1, temp - lst[n+1])
        operators[1] += 1
    
    if operators[2] != 0 : # 곱셈하는 경우
        operators[2] -= 1
        dfs(n+1, temp * lst[n+1])
        operators[2] += 1
    
    if operators[3] != 0 : #나눗셈하는 경우
        operators[3] -= 1
        dfs(n+1, int(temp/lst[n+1]))
        operators[3] += 1

dfs(0, lst[0])
print(mx)
print(mn)