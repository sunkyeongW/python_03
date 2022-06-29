#절대값

print(abs(-3))

print('--' *4)
#all, any

print(all([1,3,4])) #and의 개념
print(all([3,4,[]])) #하나의 값이라도 다를 경우 false

print(any([1,2,0])) #or의 개념

print('--' *4)
#아스키 코드(chr, ord)

print(chr(445))
print(ord('c'))

print('--' *4)
#enumerate : 인덱스 + iterable 객체 생성

for i, name in enumerate(['abc', 'ddf', 'tyf']):
    print(i, name)

print('--' *4)
#filter

def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3 , 3, 4])))
print(list(filter(lambda x : abs(x) > 2, [1, -3 , 3, 4])))
print(list(filter(lambda x : x >= 90, [1, 90 , 94, 86])))
print('--' *4)

#id
print(id(5))
print(id('d'))
print('--' *4)

#len
print(len('abcdef'))
print(len([1, 3, 43, 56, 12, 5]))
print('--' *4)
#max, min
print(max([3, 4, 7]))
print(max('python'))
print('--' *4)
print(min([3, 4, 7]))
print(min('python'))

print('--' *4)

#map

def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, 4, -3, 5, 2, -1])))
print(list(map(lambda x:abs(x),[1, 4, -3, 5, 2, -1])))

print('--' *4)

#pow
print(pow(2,10))

print('--' *4)
#range
print(range(2,10,3))
print(list(range(2,10,3)))

print('--' *4)
#round : 반올림

print(round(5.5563,2))

print('--' *4)

#sorted : 반복 가능한 객체

print(sorted([3, 4, 5, 6, 2])) #순서대로 정렬
print(tuple(sorted([3, 4, 5, 6, 2])))

a = sorted([3, 4, 5, 6, 2])
print(a)

print(sorted('python'))

print('--' *4)


#sum
print(sum([3, 4, 5, 1, 6]))
print(sum(range(1, 101)))

print('--' *4)

#type
print(type(3))
print(type([]))
print(type({}))
print(type(()))

print('--' *4)

#zip
print(list(zip([3, 4, 5],[334, 45, 6])))
print(list(zip([3, 4, 5],[334, 45, ])))

print(type(list(zip([3, 4, 5],[334, 45, 6]))[0]))