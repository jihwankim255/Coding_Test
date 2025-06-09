import sys
input = sys.stdin.readline

N = int(input())

count_5 = N // 5

count_3 = (N - count_5*5) // 3


if count_5*5 + count_3*3 == N:
    print(count_3 + count_5)
else:
    while count_5 > 0:
        count_5 -= 1
        count_3 = (N - count_5*5) // 3
        if count_5*5 + count_3*3 == N:
            print(count_3 + count_5)
            break
    if count_5*5 + count_3*3 != N:
        print(-1)