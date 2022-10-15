def print_line():
    print('-----------------------------------------------------')

# list는 순서(인덱스 번호 0 ~)를 이용하여 데이터를 관리하는 방법

# list 생성
list1 = list()
print(type(list1))
print(list1)

# list는 나중에 수정 가능 tuple은 수정 불가능!
list2 = []
print(type(list2))
print(list2)

print_line()

# 값이 있는 list 생성
list3 = [10, 20, 30, 40, 50]
print(type(list3))
print(list3)

# list 연산
list4 = list3 + [60, 70, 80, 90, 100]
print(list4)

list5 = list3 * 3
print(list5)

print_line()

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(list1[0])
print(list1[1])
print(list1[-1])
print(list1[-2])
print(list1[2:5])
print(list1[:5])
print(list1[2:])

print_line()

# list가 관리하는 값의 개수
a1 = len(list1)
print(a1)

print_line()

# list 내의 최대 최소값
list1 = [50, 20, -30, 40, 80]

a1 = max(list1)
a2 = min(list1)

print(a1)
print(a2)

print_line()

# 튜플을 리스트로 변환
tuple1 = (10, 20, 30, 40, 50)
list1 = list(tuple1)

print(type(list1))
print(list1)

# 문자열을 리스트로 변환
str1 = 'hello world!'
list2 = list(str1)
print(list2)

print_line()

# 포맷 문자열 사용
list1 = [10, 20, 30]
print(f'작업전 : {list1}')

# 내용 추가
list1.append(40)
print(f'추가후 : {list1}')

# 여러개 추가
list1.extend([50, 60, 70])
print(f'여러개 추가 : {list1}')

# 인덱스 1 위치에 90을 삽입
list1.insert(1, 90)
print(f'삽입후 : {list1}')

# 원본을 유지한 채로 가져오기
a1 = list1[0]
print(a1)
print(list1)

# 원본에서 제일 뒤의 값을 추출. 원본에서는 제거됨.
a2 = list1.pop()
print(a2)
print(list1)

# index 번째 값을 추출해 반환.
a3 = list1.pop(2)
print(a3)
print(list1)

print_line()

# 값을 지정하여 제거. 제일 왼쪽에서부터 찾아 하나를 지움.
list1 = [10, 20, 30, 40, 20, 50, 60, 20, 70]
print(list1)

list1.remove(20)
print(list1)

# 정렬 : 원본 자체를 정렬
list1.sort()
print(list1)

# 뒤집기
list1.reverse()
print(list1)

print_line()

# 값의 위치찾기. list와 tuple에서는 index 함수만 사용 가능하므로 없는 값을 입력하면 오류 발생!
list1 = [10, 20, 30, 40, 50]

a1 = list1.index(20)
print(a1)

# 없는 값을 찾으려하면 오류 발생
#a2 = list1.index(21)
#print(a2)