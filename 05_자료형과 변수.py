# 리터럴 : 프로그래밍언어에서 값을 작성하는 문법

print('정수 :', 100)
print('실수 :', 11.11)
print('문자열 :', '문자열')
print('참 :', True)
print('거짓 :', False)
print('지수 :', 2e5)
print('복소수 :', 10 + 8j)
print('세자리 마다 표시 :', 123_456_789)
print('없음 :', None)

# type : 값의 타입을 확인할 수 있는 함수
print(type(11.11))
print(type('문자열'))
print(type(True))
print(type(100))
print(type(False))
print(type(2e5))
print(type(10 + 8j))
print(type(123_456_789))

# 변수 << 메모리
# 메모리에 올린 정보를 cpu에서 연산하는 것
# 변수 사용
a1 = 100;
a2 = 11.11;
a3 = '문자열';

print(a1);
print(a2);
print(a3);

a1 = 200;
print(a1);

a1 = '문자열';
print(a1);

print(type(a1));

print('---------------------------');

a1 = a2 = a3 = 100;
print(a1);
print(a2);
print(a3);

print('---------------------------');
a1, a2, a3 = 100, 200, 300;
print(a1);
print(a2);
print(a3);

print('---------------------------');

a1 = 'Hello World';
a2 = "Hello World";
a3 = '''Hello World''';
a4 = """Hello World""";

print(type(a1));
print(type(a2));
print(type(a3));
print(type(a4));

print(a1[0]);
print(a1[1]);
print(a1[-1]);
print(a1[-2]);

# 인덱스 2부터 5-1까지
print(a1[2:5]);
# 처음부터 5-1까지
print(a1[:5]);
# 인덱스 2부터 끝까지
print(a1[2:]);

# 곱하기 : 곱하는 수 만큼 반복된 문자열
print(a1 * 3);
# 더하기 : 문자열을 합쳐준다.
print(a1 + " Test");

# 다른 타입과 더하기
print(a1 + str(100));

# 문자열을 정수나 실수로 변환
print(100 + int('100'));
print(11.11 + float('11.11'));

print('---------------------------');

list1 = [10, 20, 30, 40, 50];
print(type(list1));
print(list1);

print(list1[0]); #인덱스 0
print(list1[1]); #인덱스 1
print(list1[-1]); #뒤에서 첫번째
print(list1[-2]); #뒤에서 두번째
print(list1[1:3]); #1부터 3-1까지
print(list1[:3]); #3-1까지(0,1,2번째 출력)
print(list1[1:]); #1부터

print('---------------------------');

tuple1 = (10, 20, 30, 40, 50);
print(type(tuple1));
print(tuple1);

print(tuple1[0]); #인덱스 0
print(tuple1[1]); #인덱스 1
print(tuple1[-1]); #뒤에서 첫번째
print(tuple1[-2]); #뒤에서 두번째
print(tuple1[1:3]); #1부터 3-1까지
print(tuple1[:3]); #3-1까지(0,1,2번째 출력)
print(tuple1[1:]); #1부터

#list는 생성 후 값을 추가하거나 변경하는 것이 가능
#tuple는 한 번 생성하면 그 값을 추가하거나 변경하는 것이 불가능

print('---------------------------');

#dictionary : 이름을 가지고 데이터를 관리하는 요소

dict1 = {
        'v1' : 100,
        'v2' : 11.11,
        'v3' : '문자열'
}

print(type(dict1));
print(dict1);

#dict는 순서에 대한 개념이 없으므로, 이름을 가지고 값을 가져옴

print(dict1['v1']);
print(dict1['v2']);