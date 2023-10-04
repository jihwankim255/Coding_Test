'''
계수정렬
시간 복잡도와 공간 복잡도는 모두 O(N+K)
심각한 비효율성을 초래할 수 있음
동일한 값을 가지는 데이터가 여러 개 등장할 때 효율적임
범위만큼 메모리를 사용하여 공간복잡도가 높지만, 조건부 퀵정렬보다 빠름
'''
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')