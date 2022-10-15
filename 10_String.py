def print_line():
    print('-----------------------------------------------------')

#문자열 생성
str1 = '안녕하세요'
str2 = "안녕하세요"

print(type(str1))
print(type(str2))
print(str1)
print(str2)

# ''' ''', """ """ : 여러 줄 이거나 따옴표를 포함할 때?

str1 = "이름은 '홍길동' 입니다."
str2 = '이름은 "홍길동" 입니다.'
print(str1)
print(str2)

str3 = '''이름은 "홍길동" 이고 나이는 '30살' 입니다.'''
str4 = """이름은 "홍길동" 이고 나이는 '30살' 입니다."""
print(str3)
print(str4)

str5 = '''
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세
'''
print(str5)

str6 = """동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세"""
print(str6)

print_line()

a1 = '홍길동'
a2 = 30
a3 = 180

# 이름은 홍길동이고 30살 입니다. 홍길동의 키는 180cm 입니다. 만들어보기

# str1 = '이름은 '+a1+'이고 나이는 '+a2+'살 입니다. '+a1+'의 키는 '+a3+'cm 입니다.'
#print(str1)
#문자열과 정수값을 더하려고하니까 오류가 발생함 그래서 a2, a3를 str로 묶어줘야함(형변환)

str1 = '이름은 '+a1+'이고 나이는 '+str(a2)+'살 입니다. '+a1+'의 키는 '+str(a3)+'cm 입니다.'
print(str1)

str2 = '이름은 %s이고 나이는 %d살 입니다. %s의 키는 %dcm 입니다.' % (a1, a2, a1, a3)
print(str2)

#format과 인덱스를 이용한 방법
str3 = '이름은 {0}이고 나이는 {1}살 입니다. {0}의 키는 {2}cm 입니다.'.format(a1, a2, a3)
print(str3)

#format 문자열 이용
str4 = f'이름은 {a1}이고 나이는 {a2}살 입니다. {a1}의 키는 {a3}cm 입니다.'
print(str4)

print_line()

# 문자열 내의 문자 접근
str1 = "안녕하시렵니까"

print(str1[0])
print(str1[1])

print(str1[-1])
print(str1[-2])

# 인덱스 2 ~ 5-1까지
print(str1[2:5])

# 처음부터 5-1까지
print(str1[:5])

# 인덱스 2 ~ 끝까지
print(str1[2:])

print_line()

# 문자열 + 문자열 : 두 문자열을 합친 새로운 문자열을 생성한다. 문자열끼리만 더할 수 있음!
str1 = '문자열1' + '문자열2'
print(str1)

# 문자열 * 정수 : 곱하는 수 만큼 반복된 문자열을 생성한다.
str3 = '문자열' * 3
print(str3)

# 글자 수
str1 = 'abcdefg'
str2 = '가나다라마바사'

a1 = len(str1)
a2 = len(str2)

print(a1, a2)

print_line()

# 첫 글자를 대문자로 변환
str1 = "hello world"
str2 = str1.capitalize()

print(str1)
print(str2)

print_line()

str1 = 'python'

# 주어진 문자열을 주어진 크기로 늘려줌
# 원본 문자열을 가운데 배치하고 나머지 부분은 주어진 문자열로 채워준다.
str2 = str1.center(40, '~')
print(str2)

# 원본 문자열을 좌측에 배치하고 나머지 부분은 ~
str3 = str1.ljust(40, '~')
print(str3)

# 오른쪽 배치하고 나머지 ~
str4 = str1.rjust(40, '~')
print(str4)

print_line()

# 주어진 문자열 내에 특정 문자열이 몇 번 들어가 있는지
str1 = 'abcd abcd abcd aaaa'

a1 = str1.count('abcd')
print(a1)

# 문자열 내에 a가 몇 개 있는지
a2 = str1.count('a')
print(a2)

# 앞에서부터 10글자를 제외하고 a가 몇 개 있는지. 글자 수는 공백 포함임!!
a3 = str1.count('a', 10)
print(a3)

# 앞에서 부터 10글자를 제외하고 인덱스 15부터 끝까지의 범위를 제외한 a가 몇개가 있는지.
a4 = str1.count('a', 10, 15)
print(a4)

print_line()

# 문자열이 abc로 시작하는지
str1 = 'abcdefg'
a1 = str1.startswith('abc')
a2 = str1.startswith('zzz')

print(a1)
print(a2)

# 문자열이 efg로 끝나는지
a3 = str1.endswith('efg')
a4 = str1.endswith('zzz')

print(a3)
print(a4)

print_line()

str1 = 'abcdefg'

# cde가 어디있는지
a1 = str1.find('cde')
a2 = str1.index('cde')

print(a1)
print(a2)

# -1이 출력될것
a3 = str1.find('zzz')
print(a3)

# index는 에러뜸
# a4 = str1.index('zzz')
# print(a4)

print_line()

# 숫자(num)와 문자(alpha)로 구성되어 있는지
str1 = 'abcd1234'
str2 = 'abcdefg'
str3 = '123456'

a1 = str1.isalnum()
print(a1)

# 문자로만
a2 = str2.isalpha()
print(a2)

# 숫자로만
a3 = str3.isdigit()
print(a3)

# 소문자나 대문자로 구성되어 있는지

str4 = 'abcdefg'

a4 = str4.islower()
print(a4)
a5 = str5.isupper()
print(a5)

print_line()

# 주어진 구분자로 튜플이나 리스트가 갖고 있는 값을 병합하여 문자열을 생성
str1 = '-'
str2 = ['aaa', 'bbb', 'ccc']

str3 = str1.join(str2)
print(str3)

# 리스트나 튜플에 문자열이 아닌 것이 포함되어 있으면 오류가 발생. 문자열로만 구성되어있어야 함.
#str4 = ['aaa', 100, 11.11]
#str5 = str1.join(str4)
#print(str5)

print_line()

str1 = 'AbCdEfG'

# 대문자를 소문자로 변환
str2 = str1.lower()
print(str2)

# 소문자를 대문자로 변환
str3 = str1.upper()
print(str3)

print_line()

# 지정된 문자열의 일부를 다른 문자열로 변경
str1 = 'abcdefg' 

# cde를 zzzz로 바꿈
str2 = str1.replace('cde', 'zzzz')
print(str2)

print_line()

# 띄어쓰기를 기준으로 문자열을 나눔. 결과값은 리스트로 반환.
str1 = 'ab cd_ef gh'

a1 = str1.split()
print(a1)

# 구분자를 지정하여 문자열을 나눔.
a2 = str1.split('_')
print(a2)
