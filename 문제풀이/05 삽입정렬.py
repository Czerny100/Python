# [1] 초기 리스트 값 설정 
lst = [4, 8, 1, 5, 7, -11, 0]
print('[1] 정렬 전 :', lst)

# [2] 반복문을 돌면서 자기 위치 찾아가기 --> 삽입 정렬 알고리즘

for i in range(1, len(lst)):
    # 첫 번째 요소까지 역순으로 진행하면서 삽입 위치 찾기
    while lst[i-1] > lst[i]:
        lst[i-1], lst[i] = lst[i], lst[i-1]
        i -= 1
        if i == 0:
            break
# [3] 최종 정렬된 리스트 값 출력
print('[3] 정렬 후 :', lst)