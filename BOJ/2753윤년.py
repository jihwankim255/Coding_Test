N =  input()

if int(N) % 4 == 0 and (int(N) % 100 !=0 or int(N) % 400 == 0):
    print(1)
else:
    print(0)