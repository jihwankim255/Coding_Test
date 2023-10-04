def solution(arr1, arr2):
    answer = []
    # 행 탐색
    for i in range(len(arr1)):       
        
        temp = []
        # arr2의 열 만큼 반복
        for k in range(len(arr2[0])):
            # 각 원소 탐색
            sum = 0
            for j in range(len(arr1[0])):
                    sum += arr1[i][j] * arr2[j][k]
            temp.append(sum)
        answer.append(temp)
    return answer

#32분
# print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))

# 39분
def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        # 캐시 안에 있을 경우
        city = city.lower()
        if city in cache:
            cache.pop(city)
            cache.append(city)
            answer += 1
        else:
            # 캐시 사이즈가 작으면 추가
            if len(cache) < cacheSize:
                cache.append(city)
            # 캐시 사이즈가 꽉 찼을 경우
            else:
                cache.append(city)
                cache.pop(0)
            answer += 5
    return answer
# print(solution(	2, [ "newyork","newyork","seoul","newyork","newyork","newyork","newyork"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 우수 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
