# 사용자가 입력한 문자열을 거꾸로 출력시키는 함수를 구현하시오.

# [1] 함수 작성
def reverse_txt(str):
    print(str[::-1])

# [2] 사용자 입력
txt = input('2개 이상의 문자를 입력해주세요 :')

# [3] 함수 호출
print('[출력 결과]')
reverse_txt(txt)