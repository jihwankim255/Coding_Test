import copy   # 1시간 21분 변수 초기화 부분에서 실수했다. 앞으로 변수 초기화를 신경쓰자
def solution(want, number, discount):
    answer = 0
    dic = dict()
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for i in range(len(discount)):
        combo = 0
        temp_dic = copy.deepcopy(dic)
        if discount[i] in temp_dic and temp_dic[discount[i]] > 0:
                temp_dic[discount[i]] -= 1
                combo += 1
        # elif :
        else:
            combo = 0
            temp_dic = copy.deepcopy(dic)
            continue
        for j in range(i + 1, len(discount)):
            if discount[j] in temp_dic and temp_dic[discount[j]] > 0:
                temp_dic[discount[j]] -= 1
                combo += 1
            else:
                break
            if combo == 10:
                answer += 1
    return answer

print(solution(["banana"],[10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["banana", "apple", "rice", "pork", "pot"],
[3, 2, 2, 2, 1],
["apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana", "chicken", "apple"]))
# ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]