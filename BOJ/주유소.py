import sys
input = sys.stdin.readline

N = int(input())

distances = list(map(int,input().split()))
prices = list(map(int,input().split()))

temp = [distances[0]]
now_price_idx = 0
result = 0
for i in range(1, N-1):
    if  prices[i] >= prices[now_price_idx]:
        temp.append(distances[i])
    else:
        result += sum(temp) * prices[now_price_idx]
        temp = [distances[i]]
        now_price_idx = i
if temp:
    result+= sum(temp) * prices[now_price_idx]


print(result)

'''

아 잘못구했다. distance를 합해야함
i = 2
result = 10

temp = [ 2,4 ]
idx =   1


N = 4
N-1 = 3
'''
