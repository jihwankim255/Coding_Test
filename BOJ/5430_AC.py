import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
for _ in range(T):
    p = list(input().strip())
    n = int(input().strip())
    arr = input().strip()
    r_count = 0
    if n == 0:
        arr = []
    else:
        arr = deque(list(map(int, arr[1:-1].split(","))))
    try:
        for ele in p:
            if ele == "R":
                r_count += 1
            elif ele == "D":
                if r_count % 2 == 0:
                    arr.popleft()
                elif r_count % 2== 1:
                    arr.pop()
        if r_count % 2 == 0:
            print(f"[{','.join((map(str,arr)))}]")
        elif r_count % 2== 1:
            arr.reverse()
            print(f"[{','.join((map(str,arr)))}]")
    except:
        print("error")
        
        
    
    
'''
방해요소 '[', ']' 를 빼고 문자열로 바꾸는 법에서 시간 소요
아이디어는 맞았음
구현에서 틀림
틀린 유형: 아이디어/구현 실수/ 조건 해석 오류

deque는 pop, popleft가 있다.
리스트를 그대로str로 바꾸면 중간에 띄어씍가 포함되기 때문에 ','.join()을 써야한다
join 내부 리스트에는 문자열이 와야한다.
'''