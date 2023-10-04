def solution(name):
    arr = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    default = len(name) * "A"
    for idx, item in enumerate(default):
        if default[idx] == name[idx]:
            arr.append(1)
        else:
            arr.append(0)
        
    # 일렬로 갔을 때
    len(arr) - 1
    # 회귀했을 때
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += i
            break
    count = (count - 1) * 2
    for i in range(len(arr)-1, 0, -1):
        if arr[i] == 1:
            count += len(arr) - i
            break
    if len(arr) - 1 < count:
        pass
    else:
        ''
    return count


print(solution("JERAAAAAAAON"))