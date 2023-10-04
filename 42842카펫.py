import math
def test(a):
    if len(a) % 2:
        a = a[math.floor(len(a) / 2):]
    else:
        a = a[int(len(a) / 2):]
    return a

a = [1,3,9]
b = [1, 2, 4, 8]

# print(test(a))
# print(test(b))

################################################################

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0 and 2*(i + red//i) == brown-4:
            return [red//i+2, i+2]
        

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))