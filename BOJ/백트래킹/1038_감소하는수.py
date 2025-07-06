'''
경우의수를 구할땐 반사적으로 백트래킹을 사용

동일한 수는 감소가 아니므로 중복 불가
0~9 중에 선택하므로 최대는 9876543210
1~10까지 자리수 중에
경우의수는?

987
986

'''

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

nums = []

for i in range(1,11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        nums.append(int("".join(map(str, num))))
        
nums.sort()
print(nums[N] if len(nums) > N else -1)  
