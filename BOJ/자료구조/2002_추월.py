import sys
input = sys.stdin.readline

N = int(input())

dic = {}
arr = []
count = 0
for i in range(N):
    v = input().strip()
    dic[v] = i
for i in range(N):
    arr.append(dic[input().strip()])

for i in range(N):
    flag = False
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            flag = True
            
    if flag:
        count += 1
print(count)

'''
range를 (i+1, N-1) 했더니 안됨. (i+1, N)하니까 됨
'''