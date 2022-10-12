#while문은 조건식이 참일 경우 반복하는 구문
#while(조건식):
#     구문1
#     구문2
#의 형태

a1 = 0

while a1 < 10 :
    print('while - a1 :', a1)
    a1 = a1 + 1

#a1이 10보다 작은 경우 a1의 값에 1씩 더하면서 반복

#for in 문
#주어진 리스트나 문자열의 길이만큼 반복하는 구문
#반복할 때 지정한 변수에 리스트나 문자열의 값을 하나씩 넣어줌

a2 = [10, 20, 30, 40, 50]

for v2 in a2 :
    print('for - v2 :', v2)

#range를 사용하면 0부터 특정 숫자만큼의 값을
#관리하는 요소를 생성할 수 있음
#내가 코드를 n번 반복하겠다 할 때 range(n)의 형태로 씀
for v3 in range(5) :
    print('for v3 :', v3)

a4 = 'python'
for v4 in a4 :
    print('for v4 :', v4)
#문자열의 길이만큼 반복을 함. 한글자씩 추출해 변수에 담음

a5 = [0, 1, 2, 3, 4]

for v5 in a5 :
    if v5 > 2 :
        break

    print(v5)

for v6 in a5 :
    if v6 % 2 == 0 :
        continue

    print(v6)

#break문은 반복문의 수행을 중지 시키는 구문
#continue문은 반복문의 구문 중 continue 이후의 구문을 수행하지 않고
#다음 반복을 수행하는 구문
