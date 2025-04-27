import math

a = int(input())
fac = str(math.factorial(a))
for i in range(len((fac)), 0, -1):
    if fac[i-1] != "0":
        print(len((fac))-i)
        break
