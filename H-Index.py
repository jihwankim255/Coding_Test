'''
https://school.programmers.co.kr/learn/courses/30/lessons/42747
Lv. 2	40,551명	64%

1시간 16분 소요. 사실상 틀린문제,
0일 때 처리를 해주어야 한다.
수학 문제처럼 패턴 분석하여 공식 도출해야됨
'''
def solution(citations):
    h = max(citations)
    citations.sort(reverse=True)
    for i in range(h, 0, -1):
        # i는 가장큰 값부터 1씩 감소
        for j in range(len(citations)):

            if i > citations[j]:
                if i <= j:
                    return i
                else: break
            elif i == citations[j] and j == len(citations) -1 and len(citations) > i:
                return i
    return len(citations)
                

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
        
        
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
     
print(solution([3,0,6,1,5]))
print(solution([3,0,6,1,3,5]))
print(solution([0,0]))