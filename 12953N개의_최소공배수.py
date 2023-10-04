def solution(arr):
    answer = 1
    num = dict()
    for a in arr:
        # 
        temp = dict()
        for prime in  prime_factors(a):
            if prime in temp:
                temp[prime] += 1
            else:
                temp[prime] = 1

        for key in temp.keys():
            if key in num and temp[key] > num[key]:
                num[key] = temp[key]
            elif key not in num:
                num[key] = temp[key]
    
    for n in num.keys():
        answer *= n**num[n]
            

    return num

# def get_divisors(number):
#     divisors = set()
#     for i in range(2,int(number**(1/2))+1):
#         if (number % i) == 0:
#             divisors.add(i)
#             divisors.add(number // i)

#     return divisors

def prime_factors(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1

    return factors


print(prime_factors(6))
print(prime_factors(8))
print(prime_factors(36))
print(prime_factors(14))

print(solution([2,6,8,14]))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

print(nlcm([2,6,8,14]))

# 한개씩 최소공배수를 구하면서 쌓으면 n개의 최소공배수가 된다 a * b / gcd(a, b)