# 리스트 내 요소 값들을 하나의 문자열로 이어서 출력시키는 함수를 구현하시오.
# 이때 문자 사이사이에 별표(*)를 넣어서 아래의 결과처럼 출력시키시오.
# 이 문제는 리스트를 문자열로 바꿀수 있는지를 묻는 문제이다.
# join() 함수의 사용법을 알고있는지를 묻는 문제이다.

# [1] 함수 작성 >> 리스트를 문자열로 변환 >> ''.join()
def convert_lst_str(str):
    return '*'.join(str)

# [2] 리스트
sample_txt = ['k','o','r','e','a']
print('[2] 리스트: ', sample_txt)

# [3] 함수 호출하여 결과 출력
result = convert_lst_str(sample_txt)
print('[3] 리스트를 문자열로 변환',result,type(result))