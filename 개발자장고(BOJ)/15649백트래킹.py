'''
https://youtu.be/atTzqxbt4DM?si=Q9aZlgp9T5tMotzv
https://www.acmicpc.net/problem/15649

개념
- 모든 경우의 수를 확인해야 할 때
  - for로는  확인이 불가한 경우(깊이가 달라질 때) ex) 순열

시간 복잡도(최대 2억개가 넘지 않아야 한다. 10언저리)
- N^N: 중복이 가능, N=8까지 가능
- N!: 중복이 불가, N=10까지 가능

자료 구조
- 방문 여부 확인 배열: bool[]ㅇㅇㅇㅇㅇㅇㅇ
- 선택한 값 입력 배열: int[]
-------------------------------------------------------
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문여부 확인)
- 재귀함수에서 M개를 선택할 경우 print
2. 시간복잡도
- N! > 가능
3. 자료구조

'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
chk = [False] * (N + 1)
result = []

def recur(num):
    if num==M:
        print(' '.join(map(str, result)))  
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            result.append(i)
            recur(num+1)
            chk[i] = False
            result.pop()


recur(0)