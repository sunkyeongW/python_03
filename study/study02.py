#파이썬 데이터 타입

#02.문자형 데이터 타입

print('Hello Python')
print("'3'+'4'",'3'+'4')
print('Hello Python' * 10)
print(len('Hello Python'))

#모듈 이용
print('Hello world'.replace('world', 'star'))

#이스케이프 문자 사용
print("/'=",'Hello\' Python')
print('/b =','Hello\b Python')
print('/f =','Hello\f Python')
print('/n =','Hello\n Python')
print('/t =', 'Hello\t Python')

#raw string
#이스케이프 문자 처리 무효화
raw1 = r'D://python_03'

print(raw1)

#멀티라인 입력
multi_str=\
'''
line
text
test
'''

print(multi_str)

#문자열 연산
str_01 = "python"
str_02 = "Apple"
str_03 = "How are you?"
str_04 = "Seoul, Busan, Incheon"

print(str_01 * 3)
print(str_02 +" "+ str_03)
print('y' in str_02)
print('a' not in str_02)

#문자열 함수
print(str_01.capitalize())
print(str_02.endswith('e'))
print(str_04.replace('Seoul','DaeJeon'))
print(sorted(str_03))
print(str_04.split(','))


#슬라이싱 연습
str_s1 = "Nice Boy"

print(str_s1[0: 3])
print(str_s1[:7])
print(str_s1[0: 3: 2])
print(str_s1[-5:])
print(str_s1[::-1])

#아스키 코드
a = 'f'
print(ord(a))
print(chr(122))