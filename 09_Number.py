import math #모듈이라고 하는건데 미리 작성해둔 파이썬 코드
import random

# # 절대값 abs
# a1 = abs(30)
# a2 = abs(-30)

# print(a1)
# print(a2)

# # 소수점 이하 올림 ceil
# a1 = math.ceil(100)
# a2 = math.ceil(55.55)
# a3 = math.ceil(-55.55)

# print(a1)
# print(a2)
# print(a3)

# # 소수점 이하 내림 floor
# a1 = math.floor(100)
# a2 = math.floor(55.55)
# a3 = math.floor(-55.55)

# print(a1)
# print(a2)
# print(a3)

# # 주어진 값에서 최소 최대값을 가져옴 min max
# a1 = min(30, -10, -20, 40)
# a2 = max(30, -10, -20, 40)

# print(a1)
# print(a2)

# # 소수점 이하 반올림 round
# a1 = round(22.22)
# a2 = round(55.55)

# print(a1)
# print(a2)

# # 소수점 이하 두 번째 자리를 기준으로 반올림
# a3 = round(55.55, 1)
# # 1의 자리를 기준으로 반올림
# a4 = round(55.55, -1)

# print(a3)
# print(a4)

# # 리스트, 튜플 등이 가지고 있는 값에서 랜덤하게 하나를 추출
# array1 = [10, 20, 30, 40, 50]

# a1 = random.choice(array1)
# a2 = random.choice(array1)
# a3 = random.choice(array1)

# print(a1)
# print(a2)
# print(a3)

# str1 = 'Hello World'
# a4 = random.choice(str1)

# print(a4)

# 0에서 99 사이의 정수값 하나를 랜덤하게 추출
a1 = random.randrange(100)
print(a1)

# 5에서 30 사이의 정수값 하나를 랜덤하게 추출
a2 = random.randrange(5, 31)
print(a2)

# 5에서 30 사이이고 2씩 증가된 숫자 중 하나를 추출
a3 = random.randrange(5, 31, 2)
print(a3)

# 0 ~ 1 보다 작은 실수 중에 랜덤하게 추출
a1 = random.random()
print(a1)