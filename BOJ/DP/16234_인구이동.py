import sys
input = sys.stdin.readline

N = int(input())
dp = [2,3,5,7]


def isPrime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            return flag
    return flag

for _ in range(1, N):
    temp = []
    for prime in dp:
        #  1~9 까지를 넣은 수
        for i in range(1, 10, 2):
            v = str(prime) +  str(i)
            v = int(v)
            if isPrime(v):
                temp.append(v)
    dp = temp
    
for i in dp:
    print(i)


'''
1자리 소수 구하기 
1~9


2자리 소수 구하기 = 1자리 소수 + 1~9
3자리 소수 구하기 = 2자리 소수 + 1~9

1 <= N <= 8

N
dp 4, 
5

'''
