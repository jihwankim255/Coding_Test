''' 
https://school.programmers.co.kr/learn/courses/30/lessons/42885
탐욕법(Greedy)
Lv. 2	28,718명	69%
몸무게 큰사람은 어차피 for문 한번마다 제거되므로, 내림차순 정렬
작은 사람은 limit이하일 때에만 제거됨. 이미 제거되면 카운트할 필요 없기 때문에 pop()
'''

# def solution(people, limit):
#     boat = 0
#     weight = 0
#     count = 0
#     people.sort(reverse = True)
    
#     while people:
#         if len(people) <= 1: 
#             boat += 1
#             break
#         if people[0] + people[-1] <= limit:
#             people.pop(0)
#             people.pop()
#         else:
#             people.pop(0)
            
#         boat += 1
    
    
#     return boat

# def solution(people, limit):
#     boat = 0
#     people.sort(reverse = True)
    
#     while people:
#         if len(people) <= 1: 
#             boat += 1
#             break
#         target = limit - people[-1]
#         for idx, i in enumerate(people):
#             if i <= target:
#                 boat += idx + 1
#                 people = people[idx+1:-1]
            
    
#     return boat
# 다른 사람 풀이
def solution(people, limit):
    boat = 0
    people.sort(reverse = True)
    
    for person in people:
        if person + people[-1] <= limit and len(people) > 1:
            people.pop()
        boat += 1
        # people.pop(0)
    
    
            
    
    return boat

# 재 풀이 23.12.11 실패
# def solution(people, limit):
#     boat = 0
#     people.sort()
#     chk = [False] * len(people)
#     i = 0
#     small = people[i]
#     for j in range(len(people)-1, i, -1):
#         if small + people[j] <= limit:
#             chk[i] = True
#             i += 1
    
#         boat += 1
#         chk[j] = True
    
#     if not chk[i]: return boat + 1
#     return boat 


print(solution([70,80,50], 100))
print(solution([70,50,80,50], 100))
print(solution([100], 100))
print(solution([70,50,40,50,80,50,50,40,50,80,50,50,40,50,80,50,50,40,50,80,50,50,40,50,80,50], 110))