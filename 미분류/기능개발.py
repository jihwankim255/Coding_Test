import math
def solution(progresses, speeds):
    num = 0
    result = []
    queue = [i for i in progresses]
    while queue:
        count = 0
        target = math.ceil((100 - progresses[num]) / speeds[num])
        queue.pop(0)
        count += 1
        for i in range(1, len(progresses)):
            num+=1
            if progresses[i] + (speeds[i] * target) >= 100:
                count += 1
                queue.pop(0)
            else:
                break
        result.append(count)
    
        
    
    return 
print(solution([93,30,55],[1,30,5]))