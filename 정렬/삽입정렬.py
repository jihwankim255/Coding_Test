'''
삽입 정렬 O(N^2)
처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
선택정렬보다 빠르게 동작
첫 데이터는 정렬돼있다고 판단, 두번째부터 첫 데이터의 좌 우 중에 하나로 삽입
현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작함
최선의 경우 O(N)
'''
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)