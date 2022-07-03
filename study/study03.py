#파이썬 리스트 타입

#01.리스트 데이터 타입
#리스트 자료형(순서o, 중복o, 수정o, 삭제o)
#튜플 자료형(순서o, 중복o, 수정x, 삭제x)
#사전 자료형(순서x, 키 중복x, 수정o, 삭제o)


#리스트 자료형
print('리스트 자료형')
a = []
b = list()
c = [20, 30, 50, 60]
d = [23, 56, 100, 'study', 'star']
e = [26, 56.45, False, ['mouse', 'monitor']]

print(type(c),c)
print(d[0:3])
print(type(e[0] + e[1]),e[0] + e[1])
print(e[-1][1])
print(list(e[-1][1]))

#리스트 연산
print(c + d)
print(c * 3)
print('test' + str(c[0]))


print(c[:3] +c[3:])
print(c)
print(c == c[:3] +c[3:])

#id
temp = c
print(id(c))

#수정, 삭제
c[0] = 32

print(c)

c[1:2] = [3, 2, 1]

print(c)

c[1] = [3, 2, 1]

print(c)

c[1:3] = [] #삭제

print(c)

print('del')
del c[3]

print(c)

c.remove(50)
print(c)

#추가
li = [3, 5, 6, 2]

li.append(4) #맨 뒤에 추가

print(li)

li.sort() #오름차순

print(li)

li.reverse() #내림차순

print(li)

li.sort()
print(li)

li.insert(2, 8) #특정 위치에 넣고 싶을때

print(li)

li.reverse()

print(li)

print()
#pop
list = [3, 4, 5, 6, 7, 7]
print(list.pop())
print(list)
print(list.pop())
print(list)
print(list.count(7)) #원소 확인할때 유용

li.sort
print(li)

li.reverse
print(li)

ex = [34, 56]

li.extend(ex)
print(li)

