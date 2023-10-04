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
def solution(people, limit):
    boat = 0
    people.sort(reverse = True)
    
    for person in people:
        if person + people[-1] <= limit and len(people) > 1:
            people.pop()
        boat += 1
        # people.pop(0)
    
    
            
    
    return boat



print(solution([70,80,50], 100))
print(solution([70,50,80,50], 100))
print(solution([100], 100))
print(solution([70,50,40,50,80,50,50,40,50,80,50,50,40,50,80,50,50,40,50,80,50,50,40,50,80,50], 110))