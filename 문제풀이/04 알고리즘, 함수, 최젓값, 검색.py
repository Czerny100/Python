# [1] 함수 작성
def min_in_list(lst):
    # 전달 받은 리스트의 개수를 구함
    ar_num = len(lst)

    # 리스트 첫 번째 요소의 값을 first_min_number에 저장
    first_min_number = lst[0]

    for i in range(1,ar_num):
        if lst[i] < first_min_number:
            first_min_number = lst[i]
    return first_min_number

# [2] 리스트 입력 받기
lst = [33, 44, 55, 66, 77, 88, 99, 11, 22, 100, 48, 82, 57, 79, 91, 38 ]

# [3] 함수 호출하여 결과 값 출력하기
result = min_in_list(lst)
print('[3-1] 직접 구현한 min() : ', result)
print('[3-2] 내장 min()', min(lst))