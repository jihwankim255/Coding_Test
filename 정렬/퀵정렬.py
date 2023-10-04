'''
퀵 정렬 O(NlogN)  최악(N^2)
기준데이터 설정 -> 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
병합정렬과 함께 대부분 언어의 정렬 라이브러리의 근간
첫 번째 데이터를 기준 데이터(pivot)로 설정함(아무거나 가능하긴함)
피봇보다 큰수, 작은수를 찾으면 스왑하고 화살표가 엇갈리면 피봇을 삽입 나머지 재귀
'''
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start == end:
        return
    pivot = start
    left = start + 1
    right = end
    while (left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array) - 1)
print(array)
            
# 파이써닉한 퀵정렬
def pyquick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return pyquick_sort(left_side) + [pivot] + pyquick_sort(right_side)







