# [1] 사용자 입력
A, B, C, D, E = map(int, input('학생 5명의 수학 점수를 입력하세요 : ').split())
scores = [A, B, C, D, E]

sum = 0

for i in range(0, len(scores)):
    if scores[i] >= 60:
        sum += scores[i]

# [4] 출력
print(f'학생 {len(scores)}명의 입력 점수 중 60점 이상의 합계는? {sum}점 입니다.')
