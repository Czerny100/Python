# [1] 사용자 입력
scores = input('학생 5명의 수학 점수를 입력하세요 : ').split()

# [2] 입력 받은 값 >> 리스트
'''print(scores)
print(type(scores))
print(type(scores[0]))'''


# [3] 필요한 변수 선언 후 반복문을 돌면서 조건을 처리
sum = 0

for i in range(0,len(scores)):
    if int(scores[i]) >= 60:
        sum += int(scores[i])

# [4] 출력
print(f'학생 {len(scores)}명의 입력 점수 중 60점 이상의 합계는? {sum}점 입니다.')