#파이썬에서는 코드블록 {} 대신 들여쓰기로 구분

a1 = 100
a2 = 200

if a1 == 100 :
    print("a1 is 100")

if a1 != 100 :
    print("a1 is not 100")

#else는 if문의 조건식이 거짓일 경우 수행함

if a2 == 100 :
    print('a1 is 100')
else :
    print('a2 is not 100')

#elif

a2 = 200

if a2 == 100 :
    print('a2 is 100')
elif a2 == 200 :
    print('a2 is 200')
elif a2 == 300 :
    print('a3 is 300')
else :
    print('a2 is not 100, 200, 300')