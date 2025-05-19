def solution(k, tangerine):    # 40분 소요
    answer = 0
    count = 0
    d = dict()
    for tanger in tangerine:
        if tanger in d:
            d[tanger] += 1
        else:
            d[tanger] = 1 
    for v in sorted(list(d.values()), reverse=True):
        if count < k:
            count += v
            answer += 1
        else:
            break
    return answer 

print(solution(1,[1]))
print(solution(6,[1,3,2,5,4,5,2,3]))
print(solution(4,[1,3,2,5,4,5,2,3]))
print(solution(2,[1,1,1,1,2,2,2,3]))
import collections
print(collections.Counter([1,3,2,5,4,5,2,3]))