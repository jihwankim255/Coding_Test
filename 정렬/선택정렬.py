'''
선택 정렬 O(N^2) 
처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞 데이터와 바꾸는 것을 반복(왜 이름이 선택정렬임?)
for문 돌면서 제일 작은 수를 처리 안된 맨앞과 바꿈
구현 쉬운 대신 비효율적
'''
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
print(array)

a = 3
b = 5
print(a,b)  # 3 5
a, b = b, a
print(a,b)  # 5 3