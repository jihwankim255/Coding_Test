import sys
input = sys.stdin.readline

N = int(input())   
arr = list(map(int,input().split()))
M = int(input()) 

left = 1
right = max(arr)

result = 0

while left <= right:
    mid = (left + right) // 2
    
    total = 0
    for i in arr:
        if i < mid:
            total += i
        else:
            total += mid
    
    if total <= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1        
print(result)