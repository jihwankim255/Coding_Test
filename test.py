# a = [3,5,6,2,1,5,1]
# print(a)
# print(a[::-1])
# from collections import deque

# q = deque()
# q.append(3)
# q.append(5)
# q.append(3)
# q.append(1)
# q.append(2)
# q.append(8)

# q.popleft()

# print(q) 
# n = 5
# roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
# graph = [[] for _ in range(n+1)]

# for a,b in roads:
#     graph[a].append(b)
#     graph[b].append(a)
    
# print(graph)

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

citations = [3,0,6,1,5]
# print(map(min, enumerate(citations, start=1)))

# for i in enumerate(citations, start= 1):
    # print(i,"   ", min(i))
    
# print( max(map(min, enumerate(citations, start=1))))



def solution(s):
    lst = []
    for i in s:
        while len(lst) > 0 and lst[-1] < i:
            lst.pop()
        lst.append(i)

    answer = ''.join(lst)
    return answer

# print(solution('xyb'))
# print(solution('yxyc'))

def my_solution(s):
    # 전체 문자열부터 점점 시작점을 움직이면서 비교
    # 'x'보다 'x'뒤에 'y'가 추가된 'xy'가 뒤에오므로
    # 'xyb'는 'xyb', 'yb', 'b'만 비교하면 알 수 있다
    
    # 문자열 전체에 해당하는 부분부터 더 큰 값이 나오면 교체한다
    result = s
    for idx, char in enumerate(s):
        # print(idx, s[idx:])
        # 현재의 최대와 비교할 대상
        target = s[idx:]
        start = 0
        # 비교하여 교체하는 로직
        while start < len(target):
            if ord(result[start]) < ord(target[start]):
                result = target
                break
            elif ord(result[start]) is ord(target[start]):
                start += 1                
            else:
                break
    return result
# print(my_solution('yxyc'))
# print(my_solution('xyb'))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [element for element in matrix]
print(flattened)

input = '''
2 2 2
4 4 4
8 8 8
'''
print(input)