def solution(s):   # 18분 소요
    answer = 0
    for i in range(len(s)):
        if is_right(s[i:] + s[:i]):
            answer += 1


    return answer

def is_right(str):
    answer = 0
    open = "{[("
    stack = []
    for s in str:
        if s in open:
            stack.append(s)
        elif s == "}" and len(stack) > 0 and stack[-1] == "{":
            answer += 1
            stack.pop()
        elif s == "]" and len(stack) > 0 and stack[-1] == "[":
            answer += 1
            stack.pop()
        elif s == ")" and len(stack) > 0 and stack[-1] == "(":
            answer += 1
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    
    return False


print(solution("[](){}"))
print(solution("}]()[{"	))
print(solution("[)(]"))
print(solution("}}}"))


# len(stack)으로 stack[-1] 사용 가능한지 판별하는게 맞는지?