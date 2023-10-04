'''
메모리 적절한 사용, 수행 시간 효율성을 비약적으로 향상시키는 방법
이미 계산된 결과는 별도의 메모리에 저장
1.큰 문제를 작은 문제를 나누어 해결할 수 있거나
2.동일한 작은 문제를 반복적으로 해결해야 하거나
'''
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(3))


def fibo(x):
    a, b = 0, 1
    for i in range(x):
        a, b = b, a+b
    return a
    
