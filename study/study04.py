
#튜플 자료형(순서o, 중복o, 수정x, 삭제x)

a =()
b =(4,)
c =(3, 4, 6, 7)
d =(34, 24, 'a', 'b', 'c')
e =(78, 98, ('d', 'e', 'f'))

print(list(e[0:][0:3]))

#튜플 함수

li =(2, 5, 3, 7, 8)
print(li.index(3))
print(li.count(2))

#팩킹, 언팩킹

p = ('won', 'sun', 'k')

(x1, x2, x3) = p #언팩킹

print(x1, x2, x3)