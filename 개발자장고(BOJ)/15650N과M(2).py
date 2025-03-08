import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chk = [False] * (N+1)
result = []

def recur(start,num):
    if num == M:
        print(" ".join(map(str, result)))
        return
    for i in range(start, N+1):
        if chk[i] == False:
            chk[i] = True
            result.append(i)
            recur(i+1,num+1)
            chk[i] = False
            result.pop()

recur(1,0)

'''
1 2 3 4
chk= [False, False, True, False, False]
result = [2]
i=2
num=1

* 1
  * 1
  * 2
  * 3
  * 4
  

* 2
  * 1

* 3

* 4

1 2 



'''