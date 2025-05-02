'''
0.5초는 몇번 연산이지?

N=1
2x2   
0  0  =  0
0  1  =  1
1  0  =  2
1  1  =  3

0  2  =  3 + 1




(5,4) = 50

(6, 5)  = 57

포기
재귀까진 떠올랐는데 재귀로 푸는 방법을 모르겠음.

'''
# n보다 작으면서 2의제곱수중에 가장큰 수
def find_2n(n):
    
    x = 1
    while True:
        if n < 2**x:
            break
    return x-1
def solution(r, c):
    result = 0
    n = find_2n(r)
    
    
    return
#=========================
# import sys
# input = sys.stdin.readline

# n, r, c = map(int, input().split())

# def solve(n, a, b):
#     if n == 0:
#         return 0
#     else:
#         return (2 * (a%2) + (b%2)) + (4 * solve(n-1, (a//2), (b//2)))
    
    
    
# print(solve(n, r, c))
'''
이 방식이 되는건 신기하지만 응용이 힘들다.


'''
'''
n을 활용할 생각을 못함.
재귀함수 까진 알았어.
half
1 1 1
0 1 1
사분면이 어딘지 알려면 특정 값과 대소 비교를 해야한다. 
특정 값의 후보는 n 밖에 없다. 

'''
def z(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    if r < half and c < half:
        return z(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + z(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + z(n - 1, r - half, c)
    else:
        return 3 * half * half + z(n - 1, r - half, c - half)

# 입력 예시
N, r, c = map(int, input().split())
print(z(N, r, c))
